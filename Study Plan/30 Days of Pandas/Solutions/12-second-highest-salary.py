import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=["salary"])
    employee = employee.sort_values(by=["salary"], ascending=False).reset_index(drop=True)

    if employee.shape[0] < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    
    return pd.DataFrame({"SecondHighestSalary": [employee.loc[1, "salary"]]})
