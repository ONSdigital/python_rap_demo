# RAP Unit Testing Guide

## What are Unit Tests?
Unit tests are small, automated tests that check individual pieces of code (functions, classes, modules) to ensure they work as expected. In RAP (Reproducible Analytical Pipeline), unit tests help guarantee reproducibility, reliability, and transparency by catching errors early and documenting expected behavior.

## Why Unit Tests Matter in RAP
- **Reproducibility:** Tests ensure code produces the same results every time.
- **Automation:** Tests run automatically, saving time and reducing manual checking.
- **Transparency:** Tests document what your code is supposed to do, making it easier to review and maintain.
- **Quality:** Tests catch bugs and edge cases before code is used in production or shared with others.

## How Unit Tests Work in RAP
- Each module (e.g., io, cleaning, processing) has its own test file in the `tests/` folder.
- Tests use sample data and clear assertions to check expected outcomes.
- Tests should be independent, reproducible, and easy to understand.
- Run all tests with:
  ```cmd
  pytest tests
  ```
- If any test fails, review the error message, fix your code, and re-run the tests.

## Practical Tips
- Add tests for every new function or module you create.
- Use comments and docstrings to explain what each test does.
- Test edge cases and typical usage.
- Keep tests simple and focused.
