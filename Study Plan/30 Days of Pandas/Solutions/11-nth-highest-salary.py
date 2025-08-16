import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee = employee.drop_duplicates(subset=["salary"])

    employee_ordered = employee.sort_values("salary", ascending=False).reset_index(drop=True)

    if (employee_ordered.shape[0] < N) or (N <= 0):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    employee_ordered = employee_ordered.rename(columns={"salary": f"getNthHighestSalary({N})"})

    return employee_ordered.iloc[[N-1], [1]]