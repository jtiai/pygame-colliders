from typing import List, Tuple, Any

from .base import Collider
from .vector import Vector2
from .rect import Rect
from .convex import ConvexCollider


def is_ccw(points: List[List[float]]):
    assert len(points) == 3, "must be a triangle"

    return (
        (points[1][0] - points[0][0]) * (points[2][1] - points[0][1])
        - (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])
    ) > 0


def make_ear(shape: List[List[float]], ear: int) -> Tuple[List[float]]:
    length = len(shape)
    return shape[(ear - 1) % length], shape[ear], shape[(ear + 1) % length]


def compf(a: float, b: float, epsilon: float = 0.00001) -> bool:
    return a + epsilon > b and a - epsilon < b


def in_tri(point: List[float], tri: List[List[float]]) -> bool:
    # Barycentric coordinates.
    denom = (tri[1][1] - tri[2][1]) * (tri[0][0] - tri[2][0]) + (
        tri[2][0] - tri[1][0]
    ) * (tri[0][1] - tri[2][1])
    if compf(denom, 0.0):
        return False
    denom = 1.0 / denom

    # alpha = ((p2.y - p3.y)*(p.x - p3.x)  + (p3.x - p2.x)*(p.y - p3.y)) /
    #         ((p2.y - p3.y)*(p1.x - p3.x) + (p3.x - p2.x)*(p1.y - p3.y))
    alpha = denom * (
        (tri[1][1] - tri[2][1]) * (point[0] - tri[2][0])
        + (tri[2][0] - tri[1][0]) * (point[1] - tri[2][1])
    )
    if alpha < 0:
        return False

    # beta = ((p3.y - p1.y)*(p.x - p3.x) + (p1.x - p3.x)*(p.y - p3.y)) /
    #        ((p2.y - p3.y)*(p1.x - p3.x) + (p3.x - p2.x)*(p1.y - p3.y));
    beta = denom * (
        (tri[2][1] - tri[0][1]) * (point[0] - tri[2][0])
        + (tri[0][0] - tri[2][0]) * (point[1] - tri[2][1])
    )
    if beta < 0:
        return False

    return (1.0 - alpha - beta) >= 0


class ConcaveCollider(Collider):
    """
    Creates new concave collider from given list of tuples.

    Example of usage:

    .. code-block:: python

        collider_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
        collider = ConcaveCollider(collider_points)

    """

    def __init__(self, points: List[Tuple[float]], data: Any = None):
        super().__init__(data=data)
        self.points = [[x, y] for x, y in points]  # Must be mutable
        self._vertices: List[Vector2] = []
        self._colliders: List[ConvexCollider] = []

        self._setup()

    def _setup(self):
        # Triangulate before setting up vertices
        triangles = []

        shape = self.points[:]
        index = self._get_top_left_vertex(shape)

        o = is_ccw(make_ear(shape, index))

        while len(shape) >= 3:
            reflex = []
            eartip = -1

            # For each vertex in the shape
            for i in range(len(shape)):
                if eartip >= 0:
                    break

                # Create a triangle from vertex to adjacent vertices.
                tri = make_ear(shape, i)

                # If polygon's orientation doesn't match that of the triangle,
                # it's definitely a reflex and not an ear.
                if is_ccw(tri) != o:
                    reflex.append(i)
                    continue

                eartip = self._find_ear(eartip, i, reflex, shape, tri)

            if eartip == -1:
                break
            triangles.append(make_ear(shape, eartip))
            del shape[eartip]

        # Convert triangles to ConvexColliders
        self._colliders = [ConvexCollider(points) for points in triangles]

        self._setup_vertices()
        self._setup_rect()

    def _find_ear(self, eartip, i, reflex, shape, tri):
        # Test reflex vertices first.
        for x in reflex:
            # If we are testing ourselves, skip.
            if shape[x] in tri:
                continue

            # If any v in triangle, not ear.
            elif in_tri(shape[x], tri):
                break

        else:
            # No reflexes, so we test all past current vertex.
            for x in range(i + 2, len(shape)):
                if shape[x] in tri:
                    continue
                elif in_tri(shape[x], tri):
                    break

            # No vertices in the triangle, we are an ear.
            else:
                eartip = i
        return eartip

    def _get_top_left_vertex(self, shape):
        # Use orientation of the top-left-most vertex.
        left = shape[0]
        index = 0
        for x in range(len(shape)):
            v = shape[x]
            if v[0] < left[0] or (v[0] == left[0] and v[1] < left[1]):
                left = v
                index = x
        return index

    def _setup_vertices(self):
        self._vertices = [Vector2(*p) for p in self.points]

    def _setup_rect(self):
        min_x = self._vertices[0].x
        min_y = self._vertices[0].y
        max_x = self._vertices[0].x
        max_y = self._vertices[0].y
        for vec in self._vertices[1:]:
            min_x = min(vec._x, min_x)
            max_x = max(vec._x, max_x)
            min_y = min(vec._y, min_y)
            max_y = max(vec._y, max_y)

        self._rect = Rect(min_x, min_y, max_x - min_x, max_y - min_y)

    def collide(self, other) -> bool:
        """
        Check collision against the other collider.

        :param other: Other collider to check collision against.
        :type other: Collider
        :return: True if collision happens, False otherwise
        :rtype: bool
        """
        if not self._rect.collide_rect(other._rect):
            return False  # Bounding boxes don't collide
        # Concave to concave collision
        if isinstance(other, ConcaveCollider):
            for collider in self._colliders:
                if other.collide(collider):
                    return True
            return False

        # Concave to convex collision
        for collider in self._colliders:
            if collider.collide(other):
                return True
        return False

    def point_collide(self, point: Tuple[float]):
        """
        Check if point is within collider.

        .. warning:: Not implemented. Returns currently always False

        :param point: Point to test
        :type point: Tuple[float/int, float/int]
        :return: True if point is collider, False otherwise
        :rtype: bool
        """
        return False

    def _move(self, dx: float, dy: float):
        for point, vertex in zip(self.points, self._vertices):
            point[0] += dx
            point[1] += dy
            vertex.x += dx
            vertex.y += dy

        # Move sub colliders
        for collider in self._colliders:
            collider._move(dx, dy)

        # Move rect
        super()._move(dx, dy)
