# What is the `config` Folder?

The `config` folder is used to store configuration files that control how your RAP (Reproducible Analytical Pipeline) project runs. These files help separate settings from code, making your analysis easier to update, share, and reproduce.

## Why is it important?
- Keeps all important settings in one place
- Makes it easy to change file paths, parameters, or options without editing code
- Improves reproducibility and transparency
- Helps users and developers understand and customise the pipeline

## Common Types of Config Files

- **User Configuration Files** (e.g., `user_config.yaml`):
  - Store settings that anyone running the pipeline may want to change, such as:
    - File paths for input, output, or intermediate data
    - Analysis options (e.g., which months to process, which features to include)
    - Report settings (e.g., title, author, format)
    - Parameters for cleaning or processing (e.g., columns to drop, thresholds)
- **Developer Configuration Files**:
  - Store settings for developers, such as:
    - Advanced pipeline options
    - Debugging or logging settings
    - Experimental features
- **Other Config Files**:
  - You can add config files for specific tools (e.g., `pre-commit`, `pytest`, `bandit`), or for different environments (e.g., production vs. development).

## Practical Example
- In this RAP repository, `user_config.yaml` tells the pipeline where to find input data, where to save cleaned data, and where to write the final report.
- Users of the pipeline can change where files are read from or written to without updating the code.

## Summary
The `config` folder is a key part of making your RAP project flexible, reproducible, and easy to use. As your project grows, you can add more config files to organise and control different parts of your analysis.
