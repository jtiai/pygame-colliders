from typing import List, Tuple, Any
import math

from pygame_colliders import ConcaveCollider, ConvexCollider


def _cross_product_length(a, b, c):
    bax = a[0] - b[0]
    bay = a[1] - b[1]
    bcx = c[0] - b[0]
    bcy = c[1] - b[1]

    return bax * bcy - bay * bcx


def _is_convex(points):
    num_points = len(points)
    if num_points < 3:
        raise ValueError("Not a polygon")
    if num_points == 3:
        return True  # All triangles are convex

    got_negative = False
    got_positive = False
    for i_a in range(num_points):
        i_b = (i_a + 1) % num_points
        i_c = (i_b + 1) % num_points

        cross_product = _cross_product_length(points[i_a], points[i_b], points[i_c])
        if cross_product < 0:
            got_negative = True
        if cross_product > 0:
            got_positive = True

        if got_negative and got_positive:
            return False

    return True


def _is_triangle_ccw(points: List[List[float]]):
    assert len(points) == 3, "must be a triangle"

    return (
        (points[1][0] - points[0][0]) * (points[2][1] - points[0][1])
        - (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])
    ) > 0


def _is_concave(points):
    num_points = len(points)
    is_ccw = _is_triangle_ccw(points[:3])

    for i in range(num_points):
        im1 = (i - 1) % num_points
        ip1 = (i + 1) % num_points

        pt = points[i]  # Point
        ptm1 = points[im1]  # Point - 1
        ptp1 = points[ip1]  # Point + 1

        angle_in = math.atan2(ptm1[1] - pt[1], ptm1[0] - pt[0])
        angle_out = math.atan2(ptp1[1] - pt[1], ptp1[0] - pt[0])
        if is_ccw:
            angle_in, angle_out = angle_out, angle_in

        if angle_in > angle_out:
            angle_out += 2 * math.pi

        pt_angle = (angle_out - angle_in) * 180 / math.pi
        print(pt_angle)
        if pt_angle > 180:
            return True
    return False


def create_collider(points: List[Tuple[float]], data: Any = None):
    """
    Create correct collider type from given set of points.

    .. code-block:: python

        collider_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
        collider = create_collider(collider_points)

    :param points: A list of coordinate pairs that forms given collider.
    :param data: Any data associated with the collider
    :return: Correct collider type
    :rtype: ConvexCollider or ConcaveCollider
    """
    # Try out first concave
    if _is_concave(points):
        return ConcaveCollider(points, data)
    elif _is_convex(points):
        return ConvexCollider(points, data)
    else:
        raise TypeError("Invalid collider data.")
