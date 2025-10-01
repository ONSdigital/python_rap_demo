"""
Unit tests for the I/O module in the RAP pipeline.
"""
import pandas as pd
import pytest

from python_rap_demo.io import read_health_data, write_dataframe


def test_read_health_data(tmp_path):
    """
    Test reading a CSV file into a DataFrame.
    """
    # Create a temporary CSV file
    csv_path = tmp_path / "test.csv"
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df.to_csv(csv_path, index=False)
    result = read_health_data(str(csv_path))
    # Assert the DataFrame matches the original
    pd.testing.assert_frame_equal(result, df)


def test_write_dataframe(tmp_path):
    """
    Test writing a DataFrame to a CSV file.
    """
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    out_path = tmp_path / "out.csv"
    write_dataframe(df, str(out_path))
    result = pd.read_csv(out_path)
    # Assert the written file matches the original DataFrame
    pd.testing.assert_frame_equal(result, df)
