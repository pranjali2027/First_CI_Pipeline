import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_153_is_armstrong():
    assert is_armstrong(153) is True


def test_370_is_armstrong():
    assert is_armstrong(370) is True


def test_9474_is_armstrong():
    assert is_armstrong(9474) is True


def test_non_armstrong_number():
    assert is_armstrong(123) is False


def test_single_digit_number():
    assert is_armstrong(7) is True


def test_zero_is_armstrong():
    assert is_armstrong(0) is True


def test_negative_number():
    assert is_armstrong(-153) is False