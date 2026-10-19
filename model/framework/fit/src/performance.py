import json
import os

import numpy as np
import stylia
from sklearn.metrics import auc, roc_curve

# Format: slide | Style: ersilia - change with stylia.set_format() / stylia.set_style()
stylia.set_format("slide")
stylia.set_style("ersilia")

root = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.abspath(os.path.join(root, "..", "..", "..", "checkpoints"))
results_dir = os.path.abspath(os.path.join(root, "..", "results"))

DECISION_RANK = 0.65


def load_results(name):
    with open(os.path.join(model_dir, name, "report_crossval.json"), "r") as f:
        return json.load(f)


def plot_roc_curve(ax, name):
    results = load_results(name)
    nc = stylia.NamedColors()
    mean_fpr = np.linspace(0, 1, 100)
    tprs, aucs = [], []
    for i in results.keys():
        y_hat = results[i]["y_rank"]
        y_true = results[i]["y_true"]
        fpr, tpr, _ = roc_curve(y_true, y_hat)
        aucs.append(auc(fpr, tpr))
        tpr_interp = np.interp(mean_fpr, fpr, tpr)
        tpr_interp[0] = 0.0
        tprs.append(tpr_interp)
        ax.plot(mean_fpr, tpr_interp, color=nc.get("plum", lighten=0.5))
    mean_tpr = np.mean(tprs, axis=0)
    ax.plot(mean_fpr, mean_tpr, color=nc.plum,
            label="Mean ROC (AUC = {:.2f} $\\pm$ {:.2f})".format(auc(mean_fpr, mean_tpr), np.std(aucs)))
    ax.plot([0, 1], [0, 1], linestyle="--", color=nc.gray)
    ax.legend()
    stylia.label(ax, xlabel="False positive rate", ylabel="True positive rate", title=name)


def plot_rank(ax, name):
    results = load_results(name)
    nc = stylia.NamedColors()
    y_rank = np.array(results["0"]["y_rank"])
    y_true = np.array(results["0"]["y_true"])
    for y, color in ((y_rank[y_true == 0], nc.gray), (y_rank[y_true == 1], nc.plum)):
        x = 0 if color == nc.gray else 1
        ax.scatter(x + np.random.uniform(-0.1, 0.1, size=y.size), y, color=color, alpha=0.5)
    ax.axhline(DECISION_RANK, linestyle="--", color=nc.gray)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Neg", "Pos"])
    ax.set_ylim(-0.05, 1.05)
    stylia.label(ax, xlabel="", ylabel="Rank score", title=name)


fig, axs = stylia.create_figure(1, 2)
plot_roc_curve(axs.next(), "permeability")
plot_rank(axs.next(), "permeability")
stylia.save_figure(os.path.join(results_dir, "performance_5fold.png"))

results = load_results("permeability")
roc_aucs = [v["roc_auc"] for v in results.values()]
print("MEAN AUC: ", np.mean(roc_aucs), np.std(roc_aucs))
