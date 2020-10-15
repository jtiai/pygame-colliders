import pytest
from pygame_colliders import Rect


def test_basic_getters():
    r = Rect(5, 7, 11, 12)

    assert r.x == 5
    assert r.y == 7
    assert r.w == 11
    assert r.h == 12


def test_float():
    r = Rect(0.1, 7.5, 1.5, 3.33)

    assert r.x == pytest.approx(0.1)
    assert r.y == pytest.approx(7.5)
    assert r.w == pytest.approx(1.5)
    assert r.h == pytest.approx(3.33)


def test_set_right():
    r = Rect(5, 7, 11, 12)
    r.right = 20

    assert r.x == 9
    assert r.y == 7
    assert r.w == 11
    assert r.h == 12


def test_get_topleft():
    r = Rect(5, 7, 11, 12)

    assert r.topleft == (5, 7)


def test_set_topleft():
    r = Rect(5, 7, 11, 12)
    r.topleft = (42, 12)

    assert r.x == 42
    assert r.y == 12


def test_get_center():
    r = Rect(5, 7, 10, 16)

    assert r.center == (10, 15)


def test_set_center():
    r = Rect(5, 7, 10, 16)
    r.center = (42, 12)

    assert r.x == 37
    assert r.y == 4
