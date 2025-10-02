"""
Unit tests for the report module in the RAP pipeline.
"""
import os

import pandas as pd

from python_rap_demo.report import generate_markdown_report


def test_generate_markdown_report(tmp_path):
    """
    Test the generate_markdown_report function to ensure it:
    - Creates a markdown file
    - Includes expected content
    """
    # Create a sample DataFrame for the report
    df = pd.DataFrame({
        "month": ["2025-01"],
        "diagnosis": ["A"],
        "case_count": [10],
        "total": [20],
        "prevalence_rate": [0.5]
    })
    # The function will write to <output_path>/disease_prevalence_report.md
    out_dir = tmp_path
    expected_file = out_dir / "disease_prevalence_report.md"
    generate_markdown_report(df, str(out_dir) + os.sep)
    # Check that the file exists and contains expected text
    assert expected_file.exists()
    content = expected_file.read_text()
    assert "Disease Prevalence Report" in content
