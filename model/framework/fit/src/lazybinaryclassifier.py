import collections
import json
import os
import shutil

import numpy as np
import pandas as pd
from lazyqsar.qsar import LazyClassifierQSAR
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold

root = os.path.dirname(os.path.abspath(__file__))

train_file = os.path.join(root, "..", "data", "manrique_paeruginosa_permeability_standard.csv")
model_folder = os.path.join(root, "..", "..", "..", "checkpoints", "permeability")

MODE = "slow"
FOLDS = 5
SEED = 42

train = pd.read_csv(train_file)
x = train["st_smiles"].astype(str)
y = train["permeability_class"].astype(int)


def fit_and_evaluate(x_train, x_test, y_train, y_test, output_dir, mode, clean=True):
    model = LazyClassifierQSAR(mode=mode)
    model.fit(smiles_list=x_train, y=y_train)
    model.save(output_dir)
    model = LazyClassifierQSAR.load(output_dir)
    y_pred = model.predict_proba(smiles_list=x_test)[:, 1]
    y_rank = model.predict_rank(smiles_list=x_test)[:, 1]
    descriptors = json.load(open(os.path.join(output_dir, "metadata.json"))).get("active_descriptors")
    if clean:
        shutil.rmtree(output_dir, ignore_errors=True)
    return roc_auc_score(y_test, y_pred), y_pred, y_rank, descriptors


print("Crossvalidation")
roc_aucs = []
report = collections.defaultdict(dict)
skf = StratifiedKFold(n_splits=FOLDS, shuffle=True, random_state=SEED)
for fold, (train_idx, test_idx) in enumerate(skf.split(x, y)):
    output_dir = os.path.join(model_folder, f"fold_{fold}")
    X_train, X_test = x[train_idx].tolist(), x[test_idx].tolist()
    y_train, y_test = y[train_idx].tolist(), y[test_idx].tolist()
    roc_auc, y_hat, y_rank, descriptors = fit_and_evaluate(
        x_train=X_train, x_test=X_test, y_train=y_train, y_test=y_test,
        output_dir=output_dir, mode=MODE,
    )
    print(f"Fold {fold}", "AUROC", roc_auc, "descriptors", descriptors)
    report[fold]["y_true"] = list(y_test)
    report[fold]["y_hat"] = list(y_hat)
    report[fold]["y_rank"] = list(y_rank)
    report[fold]["roc_auc"] = roc_auc
    report[fold]["roc_auc_rank"] = roc_auc_score(y_test, y_rank)
    report[fold]["active_descriptors"] = descriptors
    roc_aucs += [roc_auc]

print("MEAN AUC: ", np.mean(roc_aucs), np.std(roc_aucs))

os.makedirs(model_folder, exist_ok=True)
with open(os.path.join(model_folder, "report_crossval.json"), "w") as f:
    json.dump(report, f, indent=2)

print("training final model")
# save() writes in place without clearing: in slow mode the surviving descriptor set
# varies between fits, so a previous fit's directories would otherwise linger and no
# longer match active_descriptors.
report_path = os.path.join(model_folder, "report_crossval.json")
saved_report = open(report_path).read() if os.path.exists(report_path) else None
shutil.rmtree(model_folder, ignore_errors=True)
os.makedirs(model_folder, exist_ok=True)
if saved_report is not None:
    with open(report_path, "w") as f:
        f.write(saved_report)

model = LazyClassifierQSAR(mode=MODE)
model.fit(smiles_list=x.tolist(), y=y.tolist())
model.save(model_folder)
