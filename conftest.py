import pytest

from script import NinjaBelt


@pytest.fixture
def white_belt():
    return NinjaBelt("white", 10)


@pytest.fixture
def white_belt_with_users():
    belt = NinjaBelt("white", 10)
    belt.users = ["Josh", "Tim", "Ed"]
    return belt


@pytest.fixture
def yellow_belt():
    return NinjaBelt("yellow", 50)
