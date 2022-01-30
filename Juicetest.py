from pytest import approx
from juice import calculate_discount


def test_calculate_discount_1():
    assert calculate_discount(2, True) == approx(0.2, rel=1e-2)


"""
def test_volume_of_pyramid_2():
    assert volume_of_pyramid(5, 3) == 25


def test_volume_of_pyramid_3():
    # assert volume_of_pyramid(8, 0) == 0"""
