import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    return tweets.loc[tweets["content"].apply(len) > 15, ["tweet_id"]]