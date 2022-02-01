import pytest
from pytest import approx

from juice import calculate_discount


def test_calculate_discount_1():
    assert calculate_discount(2, True) == approx(0.2, rel=1e-2)


def test_calculate_discount_2():
    assert calculate_discount(1, False) == 0


def test_calculate_discount_3():
    assert calculate_discount(3, False) == approx(0.25, rel=1e-2)


def test_calculate_discount_4():
    assert calculate_discount(3, True) == approx(0.4, rel=1e-2)


def test_calculate_discount_5():
    assert calculate_discount(4, False) == approx(0.33, rel=1e-1)


def test_calculate_discount_6():
    assert calculate_discount(5, True) == approx(0.464, rel=1e-2)


def test_calculate_discount_7():
    assert calculate_discount(6, True) == approx(0.6, rel=1e-2)


def test_calculate_discount_8():
    assert calculate_discount(10, False) == approx(0.5, rel=1e-2)


def test_calculate_discount_9():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(-2, True)
    assert str(exception_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert exception_info.type == ValueError


def test_calculate_discount_10():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(11, True)
    assert str(exception_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert exception_info.type == ValueError


def test_calculate_discount_11():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(20, False)
    assert str(exception_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert exception_info.type == ValueError


def test_calculate_discount_12():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount("x", False)
    assert str(exception_info.value) == "amount must be an int"
    assert exception_info.type == ValueError


def test_calculate_discount_13():
    with pytest.raises(ValueError) as exception_info:
        assert calculate_discount(3, "XXX")
    assert str(exception_info.value) == "member must be a Boolean"
    assert exception_info.type == ValueError