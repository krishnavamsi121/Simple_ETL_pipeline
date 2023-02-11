import pandas as pd


def extract_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df
