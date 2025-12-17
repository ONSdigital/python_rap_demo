<!--
README.md for a typical RAP (Reproducible Analytical Pipeline) project

This file provides a clear overview and guide for your analytical pipeline repository.

In a RAP project, the README is essential for:
- Describing the aims and scope of the analysis
- Documenting setup steps and usage instructions
- Outlining folder structure and key files
- Explaining how to run the pipeline, tests, and automation tools
- Sharing best practices for reproducibility, automation, and transparency

A well-written README makes your RAP project accessible and easy for others to use, review, or contribute to. Update it as your project evolves.
-->
# Work in Progress - RAP demonstration repository for Python

Welcome to the RAP (Reproducible Analytical Pipeline) demonstration repository! This repository is designed for beginners to practice RAP principles, experiment with code, and learn best practices for reproducible, automated, and transparent analytical pipelines in Python.

**This repository is still in development**

## Getting Started

1. **Fork the repository:**
   - Go to the GitHub page for this repository.
   - Click the "Fork" button in the top right to create your own copy.
   - Clone your forked repository:
     ```cmd
     git clone https://github.com/<your-username>/python_rap_demo.git
     cd python_rap_demo
     ```

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
- Write outputs and generate a markdown report in outputs
- You should see a message confirming the report was generated.

Explore the existing code and add your own to the `src/` folder.

### Practice with exercises

All exercises for RAP learning are in the `exercises/` folder. These are not part of the main pipeline, but are for practice and experimentation.

- Each exercise has its own subfolder and README with instructions.
- Work through exercises to learn how to:
  - Add new modules
  - Use config files
  - Write unit tests
  - Set up and customize pre-commit hooks
  - Apply RAP principles in real code

### Understanding the purpose of each file and folder

Information about different files and folders can be found throughout the pipeline:
  - Files: Contain information on what they are and what they are used for in a RAP in the file itself, except .secrets.baseline. .secrets.baseline information can be found in the `docs` folder
  - Folders: Contain a README to explain what the folder is for and typical files it contains
  - Scripts: Fully documented with docstrings and comments.

### Create and run tests

Test your functions by adding tests to the `tests/` folder.

Run tests with:
  ```cmd
  pytest tests
  ```

## Contributing

This repo is for learning and experimentation. If you want to contribute improvements, please read `CONTRIBUTING.md`.

## AI declaration

AI has been used in the production of this content.

---

Happy RAP coding!
