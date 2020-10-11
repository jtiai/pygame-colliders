from pygame_colliders import ConcaveCollider, ConvexCollider


def test_no_collision():
    poly_a_points = [(13, 10), (13, 3), (6, 3), (6, 10)]
    poly_b_points = [(14, 18), (15, 11), (10, 13)]

    poly_a = ConvexCollider(poly_a_points)
    poly_b = ConvexCollider(poly_b_points)

    assert poly_a.collide(poly_b) is False


def test_collision():
    poly_a = [(11, 10), (11, 3), (4, 3), (4, 10)]
    poly_b = [(13, 13), (8, 9), (7, 15)]

    p_a = ConvexCollider(poly_a)
    p_b = ConvexCollider(poly_b)

    assert p_a.collide(p_b) is True


def test_clockwise():
    poly = [(13, 13), (8, 9), (7, 15)]
    p = ConvexCollider(poly)

    assert p.is_clockwise is True


def test_counter_clockwise():
    poly = [(7, 15), (8, 9), (13, 13)]
    p = ConvexCollider(poly)

    assert p.is_clockwise is False


def test_point_collide():
    poly_points = [(7, 15), (8, 9), (13, 13)]
    point = (10, 12)
    poly = ConvexCollider(poly_points)

    assert poly.point_collide(point) is True


def test_point_not_collide():
    poly_points = [(7, 15), (8, 9), (13, 13)]
    point = (10, 7)
    poly = ConvexCollider(poly_points)

    assert poly.point_collide(point) is False


def test_concave_convex_collision():
    poly_a_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    poly_b_points = [(4.5, 3.5), (6, 2), (6, 4)]

    poly_a = ConcaveCollider(poly_a_points)
    poly_b = ConvexCollider(poly_b_points)

    assert poly_a.collide(poly_b) is True


def test_convex_concave_collision():
    poly_a_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    poly_b_points = [(4.5, 3.5), (6, 2), (6, 4)]

    poly_a = ConcaveCollider(poly_a_points)
    poly_b = ConvexCollider(poly_b_points)

    assert poly_b.collide(poly_a) is True


def test_concave_no_collision():
    poly_a_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    poly_b_points = [(6.5, 3.5), (8, 2), (8, 4)]

    poly_a = ConcaveCollider(poly_a_points)
    poly_b = ConvexCollider(poly_b_points)

    assert poly_a.collide(poly_b) is False


def test_concave_concave_collision():
    poly_a_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    poly_b_points = [(6.5, 5.5), (4.5, 5.5), (4.5, 6.5), (5.5, 6.5), (5.5, 7.5), (4.5, 7.5), (4.5, 8.5), (6.5, 8.5)]

    poly_a = ConcaveCollider(poly_a_points)
    poly_b = ConcaveCollider(poly_b_points)

    assert poly_a.collide(poly_b) is True
