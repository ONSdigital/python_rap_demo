# What is the `.github` folder?

The `.github` folder is a directory in your repository used to store files that interact with GitHub. This includes, templates for pull requests, instructions for GitHub products like Copilot and GitHub action workflows.

## Why is it important?
- For RAP projects, ensures your work is reproducible and transparent by documenting and automating key steps in workflows.
- Automates tasks like testing and code checks, so code is consistent and quality assured at every push or pull request.
- Templates and guidelines help document your process, so others can repeat your work and understand each step, making it easier to contribute.


## Common files in `.github`

- **Workflows** (`workflows/`):
  - Contains GitHub Actions workflow files (e.g., `ci.yml`) that automate tasks like running tests, checking code quality, or deploying your project. These workflows are run on a GitHub virtual machine after pushing code, or creating or amending a pull request. The outputs can be viewed in GitHub actions and will notify the developer and block merges if any errors are raised.
- **Pull request templates** (`PULL_REQUEST_TEMPLATE.md`):
  - Provides a checklist and guidance for contributors when they open a pull request, helping ensure best practices are followed.
- **Issue templates** (`ISSUE_TEMPLATE/`):
  - Helps users report bugs or request features in a consistent way.
- **Copilot instructions** (`copilot-instructions.md`):
  - Allows users to set baseline instructions for GitHub copilot to follow. Instructions are then followed for all prompts. For example, you may add "All functions must include docstrings with defined Args and Returns"

## Practical example
- In this RAP repository, `.github/workflows/ci.yml` runs automated tests every time you push code or open a pull request.
- `.github/PULL_REQUEST_TEMPLATE.md` helps contributors check their work before merging.

## Summary
The `.github` folder is a key part of making your project reproducible and easy to collaborate on. As you build more complex RAP projects, you can add more files here to automate and organise your work.
