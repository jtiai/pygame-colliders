from pygame_colliders.utils import _is_convex, _is_concave


def test_is_convex():
    poly_a_points = [(13, 10), (13, 3), (6, 3), (6, 10)]
    poly_b_points = [(14, 18), (15, 11), (10, 13)]
    poly_c_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]

    assert _is_convex(poly_a_points) is True
    assert _is_convex(poly_b_points) is True
    assert _is_convex(poly_c_points) is False


def test_is_concave():
    poly_a_points = [(13, 10), (13, 3), (6, 3), (6, 10)]
    poly_b_points = [(14, 18), (15, 11), (10, 13)]
    poly_c_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    poly_d_points = list(reversed([(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]))

    assert _is_concave(poly_a_points) is False
    assert _is_concave(poly_b_points) is False
    assert _is_concave(poly_c_points) is True
    assert _is_concave(poly_d_points) is True
