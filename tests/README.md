# RAP Unit Testing Guide

## What are Unit Tests?
Unit tests are small, automated tests that check individual pieces of code (functions, classes, modules) to ensure they work as expected.
For examples of written tests, look through the scripts in the `tests` folder of the pipeline. More information on unit tests can be found
in the QA for RAP learning resource [add link].

## Why Unit Tests Matter in RAP
- **Reproducibility:** Tests ensure code produces the same results every time.
- **Automation:** Tests run automatically, saving time and reducing manual checking.
- **Transparency:** Tests document what your code is supposed to do, making it easier to review and maintain.
- **Quality:** Tests catch bugs and edge cases before code is used in production or shared with others.

## How Unit Tests Work in RAP
- Each module (e.g., io, cleaning, processing) has its own test file in the `tests/` folder.
- Each function has one or more tests to ensure that it produces an expected output for different scenarios.
- If any test fails, the developer must review the error message, fix the code, and re-run the tests.

## How to Run Unit Tests
- To run all unit tests, open a terminal in the project root and enter:
  ```cmd
  pytest tests
  ```
- You can also run a specific test file, e.g.:
  ```cmd
  pytest tests/test_cleaning.py
  ```

## How to Add New Unit Tests
- For a new module (e.g., `src/python_rap_demo/new_module.py`):
  1. Create a new test file in the `tests/` folder, e.g., `tests/test_new_module.py`.
  2. Import the functions or classes you want to test.
  3. Write test functions using `assert` statements to check expected behaviour.
  4. Add comments and docstrings to explain each test.
- For an existing module:
  1. Open its test file in `tests/` (e.g., `tests/test_utils.py`).
  2. Add new test functions for any new code or edge cases.
  3. Follow the same style and structure as existing tests.
- Example test function:
  ```python
  def test_my_function():
      """Test that my_function returns expected result for sample input."""
      result = my_function(sample_input)
      assert result == expected_output
  ```
- After adding tests, run them to check everything works as expected.

## Practical Tips
- Add tests for every new function or module you create.
- Use comments and docstrings to explain what each test does.
- Test edge cases and typical usage.
- Keep tests simple and focused.
- Add tests for new functions when you create them.
