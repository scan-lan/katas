import pytest


@pytest.fixture(scope="function")
def empty_board():
    return [[0, 0, 0, 0, 0, 0, 0] * 10]
