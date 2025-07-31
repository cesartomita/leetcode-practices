import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    df_merge_left = pd.merge(person, address, how="left", on="personId")

    return df_merge_left[["firstName", "lastName", "city", "state"]]