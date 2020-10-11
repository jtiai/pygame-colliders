import math
from typing import List, Tuple

from .base import Collider
from .vector import Vector2
from .rect import Rect


class ConvexCollider(Collider):
    """
    Creates new convex collider from given list of tuples.

    Example of usage:

    .. code-block:: python

        collider_points = [(11, 10), (11, 3), (4, 3), (4, 10)]
        collider = ConvexCollider(collider_points)

    """
    def __init__(self, points: List[Tuple[float]]):
        self.points: List[List[float]] = [[x, y] for x, y in points]  # Must be mutable
        self._vertices: List[Vector2] = []
        self._edges: List[Vector2] = []
        self._normals: List[Vector2] = []

        self._setup()

    def _setup(self):
        self._setup_vertices()
        self._setup_edges()
        self._setup_normals()
        self._setup_rect()

    def _setup_vertices(self):
        self._vertices = [Vector2(*p) for p in self.points]

    def _setup_edges(self):
        self._edges = []
        vec_a = self._vertices[0]
        for vec_b in self._vertices[1:]:
            self._edges.append(vec_b - vec_a)
            vec_a = vec_b

    def _setup_normals(self):
        self._normals = [Vector2(-e.y, e.x) for e in self._edges]

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

    @property
    def is_clockwise(self) -> bool:
        """
        Checks if convex collider is clockwise.

        :return: True if clockwise, False otherwise
        :rtype: bool
        """
        sum_: float = 0
        prev = first = self._vertices[0]
        for cur in self._vertices[1:]:
            sum_ += (cur.x - prev.x) * (cur.y + prev.y)
            prev = cur
        # This is required to close the loop.
        sum_ += (first.x - prev.x) * (first.y + prev.y)
        return sum_ > 0

    def collide(self, other) -> bool:
        """
        Check collision against the other collider.

        :param other: Other collider to check collision against.
        :type other: Collider
        :return: True if collision happens, False otherwise
        :rtype: bool
        """
        # a = self, b = other
        from .concave import ConcaveCollider  # Late import due cyclic

        if isinstance(other, ConcaveCollider):
            # Check collision other way around
            return other.collide(self)

        normal_stack = self._vertices[:] + other._vertices[:]
        for normal in normal_stack:
            a_min = math.inf
            a_max = -math.inf
            b_min = math.inf
            b_max = -math.inf
            for v in self._vertices:
                dot = normal * v
                a_min = min(a_min, dot)
                a_max = max(a_max, dot)
            for v in other._vertices:
                dot = normal * v
                b_min = min(b_min, dot)
                b_max = max(b_max, dot)
            # Chained comparison due Cython
            if (b_min < a_min < b_max) or (a_min < b_min < a_max):
                continue
            else:
                return False
        return True

    def _make_bbox(self):
        return [
            (self._rect.left, self._rect.top),
            (self._rect.right, self._rect.top),
            (self._rect.right, self._rect.bottom),
            (self._rect.left, self._rect.bottom),
        ]

    def point_collide(self, point: Tuple[float]) -> bool:
        """
        Check if point is within collider.

        :param point: Point to test
        :type point: Tuple[float/int, float/int]
        :return: True if point is collider, False otherwise
        :rtype: bool
        """
        vertx = [v.x for v in self._vertices]
        verty = [v.y for v in self._vertices]

        nvert = len(self._vertices)

        testx = point[0]
        testy = point[1]
        c = 0
        j = nvert - 1
        for i in range(0, nvert):
            if ((verty[i] > testy) != (verty[j] > testy)) and (
                testx
                < (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i])
                + vertx[i]
            ):
                c += 1
            j = i
        if c % 2 == 1:
            return True
        return False

    def _move(self, dx: float, dy: float):
        # Move points and vertices
        for point, vertex in zip(self.points, self._vertices):
            point[0] += dx
            point[1] += dy
            vertex.x += dx
            vertex.y += dy

        # Update rect
        super()._move(dx, dy)

    def __str__(self):
        return f"[{','.join([f'[{x}, {y}]' for x, y in self.points])}]"
