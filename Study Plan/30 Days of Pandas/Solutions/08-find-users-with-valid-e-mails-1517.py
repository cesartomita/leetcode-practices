import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
        
    users_with_email_valid =  users[
        (users["mail"].str.endswith("@leetcode.com")) &
        (users["mail"].str[0].str.isalpha()) &
        (users["mail"].str.split("@").str[0].str.contains(r"[^a-zA-Z0-9@._-]", regex=True, na=False) == False) &
        (users["mail"].str.count("@") == 1)
    ]

    return users_with_email_valid[["user_id","name","mail"]]