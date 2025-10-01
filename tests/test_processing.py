"""
Unit tests for the processing module in the RAP pipeline.
"""
import pandas as pd

from python_rap_demo.processing import calculate_disease_prevalence


def test_calculate_disease_prevalence():
    """
    Test the calculate_disease_prevalence function to ensure it:
    - Calculates case counts and prevalence rates correctly
    - Returns expected columns
    """
    # Create a sample DataFrame
    df = pd.DataFrame({
        "month": ["2025-01", "2025-01", "2025-02"],
        "diagnosis": ["A", "B", "A"]
    })
    result = calculate_disease_prevalence(df)
    # Check output columns
    assert set(result.columns) == {"month", "diagnosis", "case_count", "total", "prevalence_rate"}
    # Check prevalence rates are between 0 and 1
    assert result["prevalence_rate"].between(0, 1).all()
