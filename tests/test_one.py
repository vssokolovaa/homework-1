import pytest
def summator(a, b):
    return a + b


@pytest.mark.smoke
def test_one():
    assert summator(10, 20) == 30

@pytest.mark.regression
def test_two():
    assert summator(10, 14) == 30
