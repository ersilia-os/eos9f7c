import os
import pandas as pd
from rdkit import Chem
from standardiser import standardise
import numpy as np

def standardise_smiles(smiles):
    st_smiles = []
    for smi in smiles:
        if smi is None:
            st_smi = np.nan
            st_smiles += [st_smi]
            continue
        smi = str(smi)
        smi = smi.strip()
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            st_smi = np.nan
            st_smiles += [st_smi]
            continue
        try:
            std_mol = standardise.run(mol)
            st_smi = Chem.MolToSmiles(std_mol, canonical=True)
            st_smiles += [st_smi]
        except:
            st_smi = Chem.MolToSmiles(mol, canonical=True)
            st_smiles += [st_smi]
        if std_mol is None:
            st_smi = Chem.MolToSmiles(mol, canonical=True)
            st_smiles += [st_smi]
            continue
    return st_smiles

root = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(root, "..","data", "manrique_paeruginosa_permeability.csv"))

df["st_smiles"] = standardise_smiles(df["smiles"].tolist())
df=df[~df["st_smiles"].isna()]
df.drop(columns = ["smiles"], inplace=True)

print("Total mols permeability data:", len(df))
print("Non permeable:", len(df[df["permeability_class"]==0]), "Permeable:", len(df[df["permeability_class"]==1]))
print("Active proportion:",  len(df[df["permeability_class"]==1])/len(df))
df.to_csv(os.path.join(root, "..","data", "manrique_paeruginosa_permeability_standard.csv"), index=False)