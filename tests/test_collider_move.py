from pygame_colliders import ConcaveCollider, ConvexCollider


def test_get_concave_center():
    poly_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]

    collider = ConcaveCollider(poly_points)

    assert collider.center == (4.0, 4.5)


def test_move_concave():
    poly_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]

    collider = ConcaveCollider(poly_points)

    collider.bottomright = (8, 9)

    assert collider.bottomright == (8, 9)
    assert collider.center == (7.0, 7.5)


def test_get_convex_center():
    poly_points = [(4.5, 3.5), (6, 2), (6, 4)]

    collider = ConvexCollider(poly_points)

    assert collider.center == (5.25, 3.0)


def test_move_convex():
    poly_points = [(4.5, 3.5), (6, 2), (6, 4)]

    collider = ConvexCollider(poly_points)

    collider.center = (13, 23)

    assert collider.center == (13, 23)
