# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar) v3.6.3, mode `slow`.
In `slow` mode LazyQSAR screens five descriptors (CDDD, Chemeleon, CLAMP, Morgan, RDKit) and keeps only those its
portfolio retains; for this model that is **Chemeleon** alone. CDDD was rejected as not applicable (too many
out-of-domain SMILES).

Upon 5-fold crossvalidation on train test splits (80-20%) with balanced classes, we obtain the following performance:


| **Model**       | **Data** | **Frac Actives (%)** | **AUROC ± STDev** |
|-----------------|----------|------------------|-------------------|
| permeability  | 600   | 40.83   |  0.918 ± 0.025 |

Predictions are reported as a **rank score** against a reference library of 50,000 drug-like molecules: a score of 0.65
is the library's 99th percentile, so by construction 1% of drug-like chemical space scores above it.
