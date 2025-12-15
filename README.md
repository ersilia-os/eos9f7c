# Permeation of compounds across the outer membrane of P. aeruginosa

Antibiotic compounds belonging to 16 chemical classes were evaluated for their ability to inhibit (IC50) three strains of Pseudomonas aeruginosa (wild-type, efflux-deficient, and efflux-deficient and porinated). Results were used to classify compounds as permeable and non-permeable. In the original article, MexB ensemble docking calculations and molecular dynamics simulations of the outer membrane were used used as features for a predictive model, on top of intrinsic physicochemical parameters of the molecules. Here we build a baseline model to predict permeability using LazyQSAR.

This model was incorporated on 2025-12-12.


## Information
### Identifiers
- **Ersilia Identifier:** `eos9f7c`
- **Slug:** `paeruginosa-permeation`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Pseudomonas aeruginosa`, `Gram-negative bacteria`
- **Tags:** `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of permeability across the P.aeruginosa membrane

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| permeability_proba | float | high | Probability of permeation across gram-negative membranes |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9f7c.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9f7c.zip)

### Resource Consumption
- **Model Size (Mb):** `3`
- **Environment Size (Mb):** `1916`


### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://www.nature.com/articles/s42004-024-01161-y](https://www.nature.com/articles/s42004-024-01161-y)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9f7c
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9f7c
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
