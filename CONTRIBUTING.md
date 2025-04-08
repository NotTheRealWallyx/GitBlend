# Contributing to GitBlend

Thank you for your interest in contributing to GitBlend! We welcome contributions of all kinds, including bug reports, feature requests, code contributions, and documentation improvements.

## Table of Contents

1. [Getting Started](#getting-started)
2. [How to Contribute](#how-to-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Features](#suggesting-features)
   - [Submitting Code Changes](#submitting-code-changes)
3. [Code Style Guidelines](#code-style-guidelines)
4. [Running Tests](#running-tests)
5. [Pull Request Process](#pull-request-process)

---

## Getting Started

1. Fork the repository to your GitHub account.
2. Clone your forked repository:
   ```bash
   git clone https://github.com/<your-username>/GitBlend.git
   cd GitBlend
   ```
3. Set up the development environment:
   ```bash
   poetry install
   ```

---

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue using the **Bug Report** template. Include the following details:

- A clear and concise description of the bug.
- Steps to reproduce the issue.
- Expected and actual behavior.
- Environment details (e.g., OS, Python version).

### Suggesting Features

If you have an idea for a new feature, open an issue using the **Feature Request** template. Provide:

- A summary of the feature.
- A detailed description of the feature.
- The benefits of the feature.

### Submitting Code Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add your commit message here"
   ```
3. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Open a pull request to the `main` branch of the original repository.

---

## Code Style Guidelines

- Use [Black](https://black.readthedocs.io/) for code formatting.
- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code style.
- Run `black` before committing your changes:
  ```bash
  black .
  ```

---

## Running Tests

1. Run the test suite using `pytest`:
   ```bash
   poetry run pytest
   ```
2. Ensure all tests pass before submitting your pull request.

---

## Pull Request Process

1. Ensure your pull request (PR) is linked to an issue, if applicable.
2. Fill out the provided pull request template.
3. Ensure your PR passes all CI checks.
4. Request a review from one of the maintainers.

---

Thank you for contributing to GitBlend! If you have any questions, feel free to open an issue or reach out to the maintainers.
