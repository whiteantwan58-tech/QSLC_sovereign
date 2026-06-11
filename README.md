# QSLC Sovereign - EVE_WAKE 1010

A Python project configured with automated testing and CI/CD pipelines.

## Project Overview

This is a modern Python application with:
- Automated testing suite using pytest
- Code quality checks with flake8
- GitHub Actions CI/CD integration
- GitHub Pages deployment ready

## Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/whiteantwan58-tech/QSLC_sovereign.git
cd QSLC_sovereign

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v
```

### Code Quality

```bash
# Check code style
flake8 .

# Show statistics
flake8 . --statistics
```

## Workflows

### Python Package CI/CD
- Runs on: Push to `main` and Pull Requests
- Tests: Python 3.9, 3.10, 3.11
- Tasks: Linting + Testing

### GitHub Pages Deployment
- Automatic deployment on push to main
- URL: https://whiteantwan58-tech.github.io/QSLC_sovereign/

## Project Structure

```
QSLC_sovereign/
├── tests/
│   ├── __init__.py
│   └── test_basic.py
├── .github/
│   └── workflows/
│       └── python-package.yml
├── README.md
├── requirements.txt
└── streamlit_app.py
```

## License

This project is licensed under the Apache License 2.0. See LICENSE file for details.

## Support

For issues and questions, please use the GitHub Issues section.
