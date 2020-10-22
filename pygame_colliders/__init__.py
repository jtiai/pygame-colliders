from .concave import ConcaveCollider
from .convex import ConvexCollider
from .rect import Rect
from .utils import create_collider
from .vector import Vector2

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)
