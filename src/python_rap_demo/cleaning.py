"""
cleaning.py: Data cleaning functions
"""

import pandas as pd


def clean_health_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean health data by dropping rows with missing values in key columns.

    Args:
        df (pd.DataFrame): Raw health data.

    Returns:
        pd.DataFrame: Cleaned health data with no missing values in
        critical columns.
    """
    df = df.copy()

    # Drop rows with missing values in height_cm, weight_kg, or diagnosis
    # columns
    df = df.dropna(subset=["height_cm", "weight_kg", "diagnosis"])

    # Fill missing smoker values with 'No'
    df["smoker"] = df["smoker"].fillna("No")

    # Ensure sex is uppercase
    df["sex"] = df["sex"].str.upper()

    return df
