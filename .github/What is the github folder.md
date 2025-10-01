# What is the `.github` folder?

The `.github` folder is a special directory in your repository used to store files that help automate, organise, and improve collaboration on your project on GitHub.

## Why is it important?
- It helps you set up workflows, templates, and community standards for your project.
- It makes your project easier to contribute to and maintain, especially for teams or open-source projects.
- In RAP (Reproducible Analytical Pipeline) projects, it supports automation, reproducibility, and transparency.

## Common files in `.github`

- **Workflows** (`workflows/`):
  - Contains GitHub Actions workflow files (e.g., `ci.yml`) that automate tasks like running tests, checking code quality, or deploying your project.
- **Pull request templates** (`PULL_REQUEST_TEMPLATE.md`):
  - Provides a checklist and guidance for contributors when they open a pull request, helping ensure best practices are followed.
- **Issue templates** (`ISSUE_TEMPLATE/`):
  - Helps users report bugs or request features in a consistent way.
- **Contributing guidelines** (`CONTRIBUTING.md`):
  - Explains how to contribute to the project, including coding standards and review processes.
- **Code of conduct** (`CODE_OF_CONDUCT.md`):
  - Sets expectations for behavior in your project's community.
- **Copilot instructions** (`copilot-instructions.md`):
  - Allows users to set baseline instructions for GitHub copilot to follow. Instructions are then followed for all prompts. For example, you may add "All functions must include docstrings with defined Args and Returns"
- **Other community files**:
  - You can add files like `FUNDING.yml` (for sponsorship), `SECURITY.md` (for reporting vulnerabilities), and more.

## Practical example
- In this RAP repository, `.github/workflows/ci.yml` runs automated tests every time you push code or open a pull request.
- `.github/PULL_REQUEST_TEMPLATE.md` helps contributors check their work before merging.

## Summary
The `.github` folder is a key part of making your project reproducible and easy to collaborate on. As you build more complex RAP projects, you can add more files here to automate and organise your work.
