from pygame_colliders import Vector2


def test_creation():
    v = Vector2(2, 9)

    assert v.x == 2
    assert v.y == 9


def test_subtract():
    v1 = Vector2(5, 9)
    v2 = Vector2(2, 3)

    v3 = v1 - v2

    assert v3.x == 3
    assert v3.y == 6


def test_assign_x():
    v = Vector2(2, 9)
    v.x = 12

    assert v.x == 12


def test_assign_y():
    v = Vector2(2, 9)
    v.y = 11

    assert v.y == 11


def test_xy():
    v = Vector2(2, 9)

    assert v.xy == (2, 9)


def test_set_xy():
    v = Vector2(2, 9)
    v.xy = (5, 10)

    assert v.xy == (5, 10)
