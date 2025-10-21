"""
Unit tests for the report module in the RAP pipeline.
"""
import pandas as pd

from python_rap_demo.report import format_month_section, generate_markdown_report


def test_format_month_section():
    month = "January"
    month_df = pd.DataFrame({
    "diagnosis": ["A", "B"],
    "case_count": [10, 20],
    "total": [20, 50],
    })
    month_df["prevalence_rate"] = month_df["case_count"] / month_df["total"]
    expected_output = (
        "## Month: January\n"
        "- A: 50.00% (10 cases)\n"
        "- B: 40.00% (20 cases)\n"
    )

    result = format_month_section(month, month_df)
    assert result.strip() == expected_output.strip()

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
    out_path = tmp_path / "report.md"
    generate_markdown_report(df, str(out_path))
    # Check that the file exists and contains expected text
    assert out_path.exists()
    content = out_path.read_text()
    assert "Disease Prevalence Report" in content
