# RAP Sandbox for Python

Welcome to the RAP (Reproducible Analytical Pipeline) Sandbox! This repository is designed for beginners to practice RAP principles, experiment with code, and learn best practices for reproducible, automated, and transparent analytical pipelines in Python.

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
   - Create and activate a virtual environment (recommended)
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

## RAP Practice Exercises

All exercises for RAP learning are in the `exercises/` folder. These are not part of the main pipeline, but are for practice and experimentation.

- Each exercise has its own subfolder and README with instructions.
- Work through exercises to learn how to:
  - Add new modules
  - Write unit tests
  - Set up and customize pre-commit hooks
  - Extend the pipeline
  - Apply RAP principles in real code

## How to Use the Sandbox

- **Main pipeline:** Run and explore the code in `src/` to see a working RAP pipeline.
- **Exercises:** Go to `exercises/` and follow the instructions in each exercise's README.
- **Do not edit files in `src/` unless instructed by an exercise.**
- **Unit tests:** Run tests with:
  ```cmd
  pytest tests
  ```
- **Pre-commit:** Pre-commit hooks will run automatically before each commit. You can run them manually with:
  ```cmd
  pre-commit run --all-files
  ```

## Contributing

This repo is for learning and experimentation. If you want to contribute improvements, please read `CONTRIBUTING.md`.

## License

MIT License

---

Happy RAP coding!
