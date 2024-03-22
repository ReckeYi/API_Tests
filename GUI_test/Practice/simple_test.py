import pytest
@pytest.mark.regression
def test_one_is_one(separator, all_tests):
    assert 1 == 1
    print(separator)

@pytest.mark.smoke
def test_two_is_two(separator):
    assert 2 == 2
    print(separator)

@pytest.mark.skip('Bug #1')
def test_three_is_three(separator):
    assert 3 == 2
    print(separator)
