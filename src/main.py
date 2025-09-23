# Main pipeline script for RAP demo
import os

from python_rap_demo.cleaning import clean_health_data
from python_rap_demo.io import read_health_data, write_dataframe
from python_rap_demo.processing import calculate_disease_prevalence
from python_rap_demo.report import generate_markdown_report
from python_rap_demo.utils import add_bmi_column, load_config


def main():
    """Run the RAP pipeline: I/O, cleaning, processing, reporting."""
    # Load config
    config = load_config(
        os.path.join(os.path.dirname(__file__), "..", "config", "user_config.yaml")
    )
    input_path = config["input_path"]
    cleaned_path = config["cleaned_path"]
    report_path = config["report_path"]

    # I/O: Read data
    df = read_health_data(input_path)

    # Cleaning
    df_clean = clean_health_data(df)
    df_clean = add_bmi_column(df_clean)
    write_dataframe(df_clean, cleaned_path)

    # Processing
    prevalence_df = calculate_disease_prevalence(df_clean)

    # Reporting
    generate_markdown_report(prevalence_df, report_path)
    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
