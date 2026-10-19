# Permeation of compounds across the outer membrane of P. aeruginosa

Scores how readily a compound crosses the outer membrane of Pseudomonas aeruginosa, the barrier that keeps most antibiotics out of this priority pathogen. Manrique and colleagues measured growth inhibition for 1260 antimicrobials across sixteen chemotypes against wild-type, efflux-deficient and hyperporinated strains, labelling permeators from the ratio of the last two IC50 values. Their own classifier added MexB ensemble docking and membrane dynamics descriptors; Ersilia instead provides a structure-only baseline trained with LazyQSAR. Permeation enables activity but is not activity.

This model was incorporated on 2025-12-12.Last packaged on 2025-12-15.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9f7c`
- **Slug:** `paeruginosa-permeation`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`, `Pneumonia`
- **Target Organism:** `Pseudomonas aeruginosa`
- **Tags:** `Antimicrobial activity`, `Gram-negative bacteria`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Rank score of a compounds predicted permeation of the Pseudomonas aeruginosa outer membrane (IC50 ratio above 0.5), calibrated against a reference library of 50,000 drug-like molecules. A rank score above 0.65 beats 99% of that library.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| permeability_rank | float | high | Rank score of the compound's predicted permeation across the Pseudomonas aeruginosa outer membrane. Calibrated against a reference library of 50K drug-like molecules so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9f7c](https://hub.docker.com/r/ersiliaos/eos9f7c)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9f7c.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9f7c.zip)

### Resource Consumption
- **Model Size (Mb):** `9`
- **Environment Size (Mb):** `1930`
- **Image Size (Mb):** `1939.69`

**Computational Performance (seconds):**
- 10 inputs: `32.75`
- 100 inputs: `27.74`
- 10000 inputs: `565.32`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://doi.org/10.1038/s42004-024-01161-y](https://doi.org/10.1038/s42004-024-01161-y)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
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
