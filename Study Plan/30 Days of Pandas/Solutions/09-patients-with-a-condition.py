import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    patients["split_conditions"] = patients["conditions"].str.split(" ")

    patients = patients.explode("split_conditions")

    patients = patients[patients["split_conditions"].str.startswith("DIAB1", na=False)]

    return patients[["patient_id", "patient_name", "conditions"]]