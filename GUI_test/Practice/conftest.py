import pytest


@pytest.fixture()
def separator():
    print('_' * 30)
    yield 'precondition: Testing...'  # precondition
    print(' - postcondition: Test finished')  # postcondition


@pytest.fixture(scope='session')
def all_tests():
    print('--- Before all ---')  # Ex: DB connect
    yield
    print('--- After all ---')  # Ex: DB disconnect