"""
report.py: Markdown report generation
"""

import pandas as pd


def format_month_section(month: str, month_df: pd.DataFrame) -> str:
    """
    Format the markdown section for a single month.

    Args:
        month (str): Month string.
        month_df (pd.DataFrame): DataFrame filtered for the month.

    Returns:
        str: Markdown string for the month section.
    """
    lines = [f"## Month: {month}\n"]
    for _, row in month_df.iterrows():
        lines.append(
            f"- {row['diagnosis']}: {row['prevalence_rate']:.2%} "
            f"({int(row['case_count'])} cases)\n"
        )
    lines.append("\n")
    return "".join(lines)


def generate_markdown_report(prevalence_df: pd.DataFrame, output_path: str) -> None:
    """
    Generate a markdown report of disease prevalence rates per month.

    Args:
        prevalence_df (pd.DataFrame): DataFrame with prevalence rates.
        output_path (str): Path to output markdown file.
    """
    with open(output_path, "w") as f:
        f.write("# Disease Prevalence Report\n\n")
        for month in prevalence_df["month"].unique():
            month_df = prevalence_df[prevalence_df["month"] == month]
            f.write(format_month_section(month, month_df))
