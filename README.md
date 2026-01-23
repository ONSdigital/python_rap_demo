<!--
README.md for a typical RAP (Reproducible Analytical Pipeline) project

This file provides a clear overview and guide for your analytical pipeline repository.

In a RAP project, the README is essential for:
- Describing the aims and scope of the analysis
- Documenting setup steps and usage instructions
- Outlining folder structure and key files
- Explaining how to run the pipeline, tests, and automation tools
- Any other information to help users and contributors understand and work with the project

The README file is the first file users and contributors will interact with in a RAP.
A well-written README makes the RAP project accessible and easy for others to use, review, or contribute to.
Update it as your project evolves.
-->
# Work in Progress - RAP demonstration repository for Python

Welcome to the RAP (Reproducible Analytical Pipeline) demonstration repository! This repository is designed for beginner to intermediate coders to practice RAP principles, experiment with code, and learn best practices for Reproducible Analytical Pipelines in Python.

See the [Reproducible Analytical Pipelines]([PROVISIONAL_LINK]) materials on the Analysis for Action platform for more information about RAPs and their importance.

**This repository is still in development**

## Getting Started

1. **Fork the repository:**
   - Forking means creating your own copy of this project on GitHub. Go to the [GitHub page](https://github.com/ONSdigital/python_rap_demo) for this repository (if you are not there already) and click the "Fork" button in the top right.
   - After forking, go to your new repository (it will be at `https://github.com/<your-username>/python_rap_demo`).
   - Click the green "Code" button and copy the URL shown under "Clone".
   - Open a terminal (Command Prompt) and run:
     ```cmd
     git clone https://github.com/<your-username>/python_rap_demo.git
     cd python_rap_demo
     ```
   - **Tip:** To check you are in the project root, run `dir` and make sure you see files like `README.md` and folders like `src` and `data`.

2. **Set up your environment:**
   - Create and activate a virtual environment:
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - Install dependencies:
     ```cmd
     pip install -r requirements.txt
     ```

## Repository Structure

- `src/` — Main pipeline code and modules
- `data/` — Example health data for analysis
- `config/` — Configuration files (YAML)
- `reports/` — Graphs and reports
- `tests/` — Unit tests for pipeline modules
- `exercises/` — **Practice exercises** (see below)
- `docs/` — Documentation

## Using the repository

### Run the pipeline
To run the main RAP pipeline, open a terminal in your project root and enter:

```python
src/main.py
```

This will:
- Load configuration from user_config.yaml
- Read input data from health_data.csv
- Clean and process the data
- Write the cleaned data to `data/outputs/cleaned/health_data_cleaned.csv`
- Write outputs and generate a markdown report in `data/outputs/reports/`
- You should see a message confirming the report was generated.

Explore the existing code and add your own to the `src/` folder.

### Practice with exercises

All exercises for RAP learning are in the `exercises/` folder. These are not part of the main pipeline, but are for practice and experimentation.

- Each exercise has its own subfolder and README with instructions.
- Work through exercises to learn how to:
  - Add new modules
  - Use config files
  - Write unit tests
  - Set up and customise pre-commit hooks
  - Apply RAP principles in real code

### Understanding the purpose of each file and folder

Information about different files and folders can be found throughout the pipeline:
  - Files: Contain information on what they are and what they are used for in a RAP in the file itself, except .secrets.baseline. .secrets.baseline information can be found in the `docs` folder
  - Folders: Contain a markdown (.md) file to explain what the folder is for and typical files it contains.
  - Scripts: Fully documented with docstrings and comments.

### Create and run tests

Test your functions by adding tests to the `tests/` folder.

Run tests with:
  ```cmd
  pytest tests
  ```

## Troubleshooting
If you encounter issues:
- Ensure your virtual environment is activated. The terminal prompt should show `(.venv)` at the start.
- Check that all dependencies are installed by running `pip install -r requirements.txt`.
- Verify you are in the project root directory when running commands. The terminal should show the path ending with `python_rap_demo`.
- For exercise notebooks, clean outputs and restart the kernel if you face issues.

## AI declaration

AI has been used in the production of this content.

---

Happy RAP coding!
