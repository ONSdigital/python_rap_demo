"""
cleaning.py: Data cleaning functions for RAP pipeline
"""

import pandas as pd


def clean_health_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean health data by handling missing values and standardizing columns.

    Args:
        df (pd.DataFrame): Raw health data DataFrame.

    Returns:
        pd.DataFrame: Cleaned health data DataFrame.
    """
    df = df.copy()
    # Drop rows with missing diagnosis
    df = df.dropna(subset=["diagnosis"])
    # Fill missing smoker values with 'No'
    df["smoker"] = df["smoker"].fillna("No")
    # Ensure gender is uppercase
    df["gender"] = df["gender"].str.upper()
    return df
