# Contributing to QSLC Sovereign

## How to Contribute

We welcome contributions! Here's how to get started:

### 1. Fork and Clone
```bash
git clone https://github.com/whiteantwan58-tech/QSLC_sovereign.git
cd QSLC_sovereign
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install pytest flake8
```

### 4. Make Your Changes
- Write clear, documented code
- Follow PEP 8 style guidelines
- Add tests for new features

### 5. Run Quality Checks
```bash
# Lint your code
flake8 .

# Run tests
pytest
```

### 6. Commit and Push
```bash
git add .
git commit -m "Add your feature: detailed description"
git push origin feature/your-feature-name
```

### 7. Create a Pull Request
Go to GitHub and create a PR from your branch to main.

## Code Standards

- Follow PEP 8 guidelines
- Write docstrings for all functions
- Add unit tests for new features
- Ensure all tests pass before submitting PR
- Keep commits atomic and well-documented

## Testing Requirements

All PRs must:
- Pass all existing tests
- Include tests for new features
- Maintain or improve code coverage
- Pass flake8 linting checks

## Questions?

Open an issue in the GitHub repository or check existing issues for similar topics.

Thank you for contributing!
