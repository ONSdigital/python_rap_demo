"""
io.py: Data input/output functions
"""

import pandas as pd


def read_health_data(filepath: str) -> pd.DataFrame:
    """
    Read health data CSV into a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded health data.
    """
    return pd.read_csv(filepath)


def write_dataframe(df: pd.DataFrame, filepath: str) -> None:
    """
    Write DataFrame to CSV.

    Args:
        df (pd.DataFrame): DataFrame to write.
        filepath (str): Path to output CSV file.
    """
    df.to_csv(filepath, index=False)
