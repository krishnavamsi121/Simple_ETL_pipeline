import pandas as pd


def load_data(df: pd.DataFrame) -> None:
    df.to_csv()
    # df.to_csv('s3://...')
