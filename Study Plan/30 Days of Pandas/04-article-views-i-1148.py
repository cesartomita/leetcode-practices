import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    views = views[views["author_id"] == views["viewer_id"]][["author_id"]]

    views.rename(columns={"author_id": "id"}, inplace=True)

    views.sort_values(by=["id"], inplace=True)

    views.drop_duplicates(inplace=True)
    
    return views