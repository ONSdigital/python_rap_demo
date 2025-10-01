"""
utils.py: Utility functions
"""

import pandas as pd
import yaml


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """
    Calculate BMI from height (cm) and weight (kg).

    Args:
        height_cm (float): Height in centimeters.
        weight_kg (float): Weight in kilograms.

    Returns:
        float: Calculated BMI value.
    """
    height_m = height_cm / 100
    return weight_kg / (height_m**2)


def add_bmi_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a BMI column to the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame with 'height_cm' and 'weight_kg' columns.

    Returns:
        pd.DataFrame: DataFrame with added 'bmi' column.
    """
    df = df.copy()
    df["bmi"] = df.apply(lambda row: calculate_bmi(row["height_cm"], row["weight_kg"]), axis=1)
    return df


def load_config(config_path: str) -> dict:
    """
    Load pipeline configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML config file.

    Returns:
        dict: Configuration dictionary.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
