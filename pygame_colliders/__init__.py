VERSION = (0, 1, 3)
__version__ = ".".join([str(x) for x in VERSION])

from .concave import ConcaveCollider
from .convex import ConvexCollider
from .rect import Rect
from .vector import Vector2
