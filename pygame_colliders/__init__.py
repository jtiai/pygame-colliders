from .concave import ConcaveCollider
from .convex import ConvexCollider
from .rect import Rect
from .vector import Vector2

VERSION = (0, 1, 3, "dev1")
__version__ = ".".join([str(x) for x in VERSION])
