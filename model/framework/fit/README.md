# Fit folder: paeruginosa-permeation (eos9f7c)

This folder holds the data, code and results needed to rebuild the model. It is stored with
[eosvc](https://github.com/ersilia-os/eosvc) in the **public** bucket; only this README is
tracked in git.

## Data processing

`src/data_analysis.py` standardises `data/manrique_paeruginosa_permeability.csv` into `data/manrique_paeruginosa_permeability_standard.csv`, the training set.

## Model building

`src/01_fit_oof.py` builds one LazyQSAR 3.9.3 classifier per task, in slow mode. For each task
it runs five-fold stratified out-of-fold (OOF) cross-validation (seed 42), so every compound
gets one prediction from a model that never saw it. It writes the OOF predictions and metrics to
`results/`, then trains the final model on all compounds into `model/checkpoints/<task>/`.
`src/02_performance.py` plots the OOF ROC curve and the OOF rank of actives and inactives per
task, and collects all metrics in `results/oof_metrics.json`.

```bash
cd src
OMP_NUM_THREADS=1 python 01_fit_oof.py        # or one task: python 01_fit_oof.py permeability
python 02_performance.py
```

| Task | Output column | Training file | Compounds | Actives | OOF AUROC | Descriptors in final model |
|---|---|---|---|---|---|---|
| `permeability` | `permeability_rank` | `data/manrique_paeruginosa_permeability_standard.csv` | 600 | 245 | 0.915 | chemeleon |
