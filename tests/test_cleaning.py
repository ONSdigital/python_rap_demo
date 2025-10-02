"""
Unit tests for the cleaning module in the RAP pipeline.
"""
import pandas as pd

from python_rap_demo.cleaning import clean_health_data


def test_clean_health_data():
    """
    Test the clean_health_data function to ensure it:
    - Fills missing 'smoker' values with 'No'
    - Converts 'gender' to uppercase
    - Drops rows with missing 'diagnosis'
    """
    # Create a sample DataFrame with missing and lowercase values
    df = pd.DataFrame({
        "diagnosis": ["A", None],
        "smoker": [None, "Yes"],
        "gender": ["m", "f"],
        "height_cm": [170, None],
        "weight_kg": [70, 80]
    })
    cleaned = clean_health_data(df)
    # Check that missing 'smoker' is filled
    assert cleaned["smoker"].iloc[0] == "No"
    # Check that 'gender' is uppercase
    assert all(cleaned["gender"].str.isupper())
    # Check that rows with missing 'diagnosis' are dropped
    assert cleaned["diagnosis"].notnull().all()
