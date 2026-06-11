# QSLC Sovereign - API Documentation

## Overview

QSLC Sovereign is a Python application designed with automation and testing at its core.

## API Endpoints

### Testing
- Run all tests: `pytest`
- Run specific test file: `pytest tests/test_basic.py`
- Run with coverage: `pytest --cov=.`

### Linting
- Check entire codebase: `flake8 .`
- Show statistics: `flake8 . --statistics`
- Complex report: `flake8 . --max-complexity=10`

## Integration

### GitHub Actions
The project includes automated workflows:

**Workflow: Python Package**
- Trigger: Push to main, Pull Requests
- Matrix: Python 3.9, 3.10, 3.11
- Tasks: Lint + Test

### Environment Setup

```python
# Example: Using in your application
import sys
sys.path.insert(0, '/path/to/QSLC_sovereign')

# Import tests
from tests.test_basic import test_example
```

## Example Usage

```bash
# Install and setup
pip install -r requirements.txt

# Run tests
pytest -v

# Check code quality
flake8 . --statistics --show-source
```

## Deployment

The project is configured for automatic GitHub Pages deployment on every push to main.

## Additional Resources

- See README.md for setup instructions
- See CONTRIBUTING.md for contribution guidelines
- See SECURITY.md for security policies
