import pandas as pd

def transform_data(df:pd.DataFrame) -> pd.DataFrame:
    df_album = df[df['Year Released'] > 2019]
    return df_album
