"""
Unit tests for the utils module in the RAP pipeline.
"""
import pandas as pd
import pytest

from python_rap_demo.utils import add_bmi_column, calculate_bmi, load_config


def test_add_bmi_column():
    """
    Test the add_bmi_column function to ensure it adds a 'bmi' column correctly.
    """
    df = pd.DataFrame({"height_cm": [180, 160], "weight_kg": [80, 60]})
    result = add_bmi_column(df)
    assert "bmi" in result.columns
    assert pytest.approx(result["bmi"].iloc[0], 0.01) == calculate_bmi(180, 80)


def test_calculate_bmi():
    """
    Test the calculate_bmi function for correct BMI calculation.
    """
    bmi = calculate_bmi(180, 80)
    assert pytest.approx(bmi, 0.01) == 24.69


def test_load_config(tmp_path):
    """
    Test the load_config function to ensure it loads YAML config correctly.
    """
    yaml_path = tmp_path / "config.yaml"
    yaml_path.write_text("input_path: test.csv\ncleaned_path: out.csv\nreport_path: report.md\n")
    config = load_config(str(yaml_path))
    assert config["input_path"] == "test.csv"
    assert config["cleaned_path"] == "out.csv"
    assert config["report_path"] == "report.md"
