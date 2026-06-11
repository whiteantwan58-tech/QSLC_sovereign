"""
Basic test suite to verify project setup and CI/CD pipeline.
"""

def test_example():
    """A simple test to verify the test setup works."""
    assert True


def test_arithmetic():
    """Test basic arithmetic operations."""
    assert 1 + 1 == 2
    assert 5 - 3 == 2
    assert 3 * 4 == 12


def test_string_operations():
    """Test basic string operations."""
    test_string = "hello"
    assert len(test_string) == 5
    assert test_string.upper() == "HELLO"
