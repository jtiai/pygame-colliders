from typing import Union, Tuple, List, Any

from .rect import Rect

try:
    import pygame

    HAS_PYGAME = True
except ImportError:
    HAS_PYGAME = False


class Collider:
    def __init__(self, data: Any = None):
        self._rect: Union[Rect, None] = None
        self.points: List[List[Union[float, int]]] = []
        self._data = data

    def _move(self, dx: float, dy: float):
        self._rect.x += dx
        self._rect.y += dy

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Any):
        self._data = value

    @property
    def x(self) -> float:
        """
        Left coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.x

    @x.setter
    def x(self, value: float):
        self._move(value - self._rect.x, 0.0)

    @property
    def y(self) -> float:
        """
        Top coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.y

    @y.setter
    def y(self, value: float):
        self._move(0.0, value - self._rect.y)

    @property
    def w(self) -> float:
        """
        Width of bounding box.

        :getter: the width
        :type: float, int
        """
        return self._rect.w

    @property
    def h(self) -> float:
        """
        Height of bounding box.

        :getter: the height
        :type: float, int
        """
        return self._rect.h

    @property
    def left(self) -> float:
        """
        Left coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.x

    @left.setter
    def left(self, value: float):
        self._move(value - self._rect.x, 0.0)

    @property
    def top(self) -> float:
        """
        Top coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.y

    @top.setter
    def top(self, value: float):
        self._move(0.0, value - self._rect.y)

    @property
    def right(self) -> float:
        """
        Right coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.right

    @right.setter
    def right(self, value: float):
        self._move(value - self._rect.right, 0.0)

    @property
    def bottom(self) -> float:
        """
        Bottom coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.bottom

    @bottom.setter
    def bottom(self, value: float):
        self._move(0.0, value - self._rect.bottom)

    @property
    def topleft(self) -> Tuple[float]:
        """
        Top left coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.topleft

    @topleft.setter
    def topleft(self, value: Tuple[float]):
        self._move(value[0] - self._rect.x, value[1] - self._rect.y)

    @property
    def topright(self) -> Tuple[float]:
        """
        Top right coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.topright

    @topright.setter
    def topright(self, value: Tuple[float]):
        self._move(value[0] - self._rect.right, value[1] - self._rect.y)

    @property
    def bottomleft(self) -> Tuple[float]:
        """
        Bottom left coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.bottomleft

    @bottomleft.setter
    def bottomleft(self, value: Tuple[float]):
        self._move(value[0] - self._rect.x, value[1] - self._rect.bottom)

    @property
    def bottomright(self) -> Tuple[float]:
        """
        Bottom right coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.bottomright

    @bottomright.setter
    def bottomright(self, value: Tuple[float]):
        self._move(value[0] - self._rect.right, value[1] - self._rect.bottom)

    @property
    def centerx(self) -> float:
        """
        Center x coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.centerx

    @centerx.setter
    def centerx(self, value: float):
        self._move(value - self._rect.centerx, 0.0)

    @property
    def centery(self) -> float:
        """
        Center y coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinate
        :type: float, int
        """
        return self._rect.centery

    @centery.setter
    def centery(self, value: float):
        self._move(0.0, value - self.centery)

    @property
    def center(self) -> Tuple[float]:
        """
        Center coordinate of bounding box.

        :getter: the coordinates
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.center

    @center.setter
    def center(self, value: Tuple[float]):
        self._move(value[0] - self._rect.centerx, value[1] - self._rect.centery)

    @property
    def midtop(self) -> Tuple[float]:
        """
        Center top coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midtop

    @midtop.setter
    def midtop(self, value: Tuple[float]):
        self._move(value[0] - self._rect.centerx, value[1] - self._rect.y)

    @property
    def midright(self) -> Tuple[float]:
        """
        Right center coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midright

    @midright.setter
    def midright(self, value: Tuple[float]):
        self._move(value[0] - self.right, value[1] - self.centery)

    @property
    def midbottom(self) -> Tuple[float]:
        """
        Center bottom coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midbottom

    @midbottom.setter
    def midbottom(self, value: Tuple[float]):
        self._move(value[0] - self._rect.centerx, value[1] - self._rect.bottom)

    @property
    def midleft(self) -> Tuple[float]:
        """
        Left center coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midleft

    @midleft.setter
    def midleft(self, value: Tuple[float]):
        self._move(value[0] - self._rect.left, value[1] - self._rect.centery)

    @property
    def size(self) -> Tuple[float]:
        """
        Size of bounding box.

        :getter: the size
        :type: tuple(float/int, float/int)
        """
        return self._rect.size

    @property
    def width(self) -> float:
        """
        Width of bounding box.

        :getter: the width
        :type: float, int
        """
        return self._rect.width

    @property
    def height(self) -> float:
        """
        Height of bounding box.

        :getter: the height
        :type: float, int
        """
        return self._rect.height

    if HAS_PYGAME:

        def draw(self, surface, color=(255, 255, 255), width=1):
            pygame.draw.polygon(surface, color, self.points, width)
