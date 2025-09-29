# Documentation for python_rap_demo

This folder contains documentation for the RAP demo project.

# About the .env File and PYTHONPATH

The `.env` file in this RAP project is used to set environment variables for your development and testing environment. Environment variables help configure your project without changing system-wide settings or code files.

## Why is `.env` useful?
- Ensures your code runs consistently across different computers and operating systems
- Makes it easy to set paths and other settings for tools like pytest, pre-commit, and some IDEs
- Supports reproducibility and automation, which are key RAP principles

## Why is PYTHONPATH used here?
- The `PYTHONPATH` variable tells Python where to look for modules when importing.
- In this project, the main pipeline code is inside the `src/` folder. By setting `PYTHONPATH=src`, you allow your tests and scripts to import modules from `src/python_rap_demo` without needing extra configuration or modifying sys.path in your code.
- This approach works on all operating systems and is recommended for RAP and Python package projects that use a `src/` layout.

## How to use the `.env` file
- Add environment variables as KEY=VALUE pairs (e.g., `PYTHONPATH=src`)
- Tools will read this file and apply the settings automatically when you run tests or scripts
- You can add other variables as your project grows (e.g., API keys, config paths)

For more information, see the documentation for your tools (pytest, pre-commit, etc.) and the Python docs on environment variables.
