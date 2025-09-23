"""
processing.py: Data processing functions for RAP pipeline
"""

import pandas as pd


def calculate_disease_prevalence(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate disease prevalence rates per month.

    Args:
        df (pd.DataFrame): Cleaned health data DataFrame.

    Returns:
        pd.DataFrame: DataFrame with prevalence rates per month and diagnosis.
    """
    prevalence = df.groupby(["month", "diagnosis"]).size().reset_index(name="case_count")

    total_per_month = df.groupby("month").size().reset_index(name="total")

    prevalence = prevalence.merge(total_per_month, on="month")

    prevalence["prevalence_rate"] = prevalence["case_count"] / prevalence["total"]

    return prevalence
