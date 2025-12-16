# What is the `src` folder?

The `src` folder is used to store the main source code for your RAP (Reproducible Analytical Pipeline) or Python package project. It helps keep your code organised, separate from data, tests, and configuration files.

## Why is it important?
- Keeps all source code in one place, making it easier to find and manage as your project grows.
- Prevents code from getting mixed up with data, configuration, or test files, which improves reproducibility and reduces mistakes.
- Makes testing and automation simpler, as tools can target the src folder directly.
- Follows Python and RAP best practice, so your project structure is familiar and easier for others to understand and contribute to.

## Common types of files in `src`
- **Main pipeline scripts** (e.g., `main.py`): Entry points for running your analysis
- **Modules and packages** (e.g., `python_rap_demo/`): Organised code for different parts of your pipeline (cleaning, processing, reporting, etc.)
- **Utility scripts**: Helper functions or classes used across the project
- **`__init__.py` files**: Mark folders as Python packages

## Example Structures
There is no single way to organise a RAP project. Select a structure that matches your project's scale and complexity, and prioritises clarity, maintainability, and ease of use for both yourself and future collaborators. Below are some common examples:

### 1. RAP best practice: "src layout"
```
project-root/
├── src/
│   ├── main.py
│   └── my_package/
│       ├── cleaning.py
│       ├── processing.py
│       ├── report.py
│       └── utils.py
├── data/
├── config/
├── tests/
```
- Keeps all code in `src/` and modules in a package subfolder
- Recommended for reproducibility and modularity

### 2. Flat layout (Simple Projects)
```
project-root/
├── main.py
├── cleaning.py
├── processing.py
├── report.py
├── data/
├── config/
├── tests/
```
- All code files in the root folder
- Easier for very small projects

### 3. Monorepo or multi-package layout
```
project-root/
├── src/
│   ├── package_one/
│   └── package_two/
├── data/
├── config/
├── tests/
```
- Useful for larger projects with multiple packages

### 4. Domain-driven structure
Organise code by analysis domain or business area.

```
project-root/
├── src/
│   ├── disease_analysis/
│   ├── cost_modelling/
│   └── shared_utils/
├── data/
├── config/
├── tests/
```

Useful for projects covering multiple topics or analytical domains.

### 5. Notebook-driven RAP
Main analysis in notebooks, supporting code in `src`.

```
project-root/
├── notebooks/
│   ├── analysis.ipynb
│   └── exploration.ipynb
├── src/
│   └── pipeline/
│       ├── cleaning.py
│       ├── processing.py
│       └── report.py
├── data/
├── config/
├── tests/
```

Good for exploratory analysis and teaching.

## Practical tips
- Use the "src layout" for most RAP and package projects
- Organise code into modules and packages for clarity and reusability
- Keep data, configs, and tests in their own folders
- Add docstrings and comments to help others understand your code

## Summary
The `src` folder is the heart of your RAP or package project. It keeps your code organised and makes your project easier to use, share, and maintain.

There are different ways to structure your code. Choose the one that fits your project's size and goals.
