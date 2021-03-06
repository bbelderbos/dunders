import pytest

from script import NinjaBelt


def test_str(white_belt):
    assert str(white_belt) == "White (10 pt)"


def test_repr(white_belt):
    assert repr(white_belt) == "NinjaBelt('white', 10)"


def test_comparison(white_belt, yellow_belt):
    assert yellow_belt > white_belt
    assert white_belt < yellow_belt
    assert yellow_belt != white_belt
    another_white_belt = NinjaBelt("white", 10)
    assert white_belt == another_white_belt


def test_len(white_belt_with_users):
    assert len(white_belt_with_users) == 3


def test_iteration(white_belt_with_users):
    users = [u for u in white_belt_with_users]
    assert users == ["Josh", "Tim", "Ed"]


def test_contains(white_belt_with_users):
    assert "Josh" in white_belt_with_users


def test_reversed(white_belt_with_users):
    users = white_belt_with_users[::-1]
    assert users == ["Ed", "Tim", "Josh"]


def test_callable(white_belt, capfd):
    white_belt()
    output = capfd.readouterr()[0]
    assert output.strip() == "I am callable"


def test_context_manager(yellow_belt, capfd):
    with yellow_belt as belt:
        print(belt)
    output = capfd.readouterr()[0]
    expected = (
        "upper slice of bread\n"
        "Yellow (50 pt)\n"
        "lower slice of bread\n")
    assert output == expected


def test_context_manager_always_rollback(yellow_belt, capfd):
    with pytest.raises(ValueError):
        with yellow_belt:
            raise ValueError
    output = capfd.readouterr()[0]
    expected = (
        "upper slice of bread\n"
        "lower slice of bread\n")  # always does the exit!
    assert output == expected


def test_add_hashing(yellow_belt):
    {yellow_belt: 2}
