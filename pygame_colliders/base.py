from typing import Union

from .rect import Rect


class Collider:
    def __init__(self):
        self._rect: Union[Rect, None] = None

    def _move(self, dx: float, dy: float):
        self._rect.x += dx
        self._rect.y += dy

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
    def topleft(self) -> tuple[float, float]:
        """
        Top left coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.topleft

    @topleft.setter
    def topleft(self,  value: tuple[float, float]):
        self._move(value[0] - self._rect.x, value[1] - self._rect.y)

    @property
    def topright(self) -> tuple[float, float]:
        """
        Top right coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.topright

    @topright.setter
    def topright(self, value: tuple[float, float]):
        self._move(value[0] - self._rect.right, value[1] - self._rect.y)

    @property
    def bottomleft(self) -> tuple[float, float]:
        """
        Bottom left coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.bottomleft

    @bottomleft.setter
    def bottomleft(self, value: tuple[float, float]):
        self._move(value[0] - self._rect.x, value[1] - self._rect.bottom)

    @property
    def bottomright(self) -> tuple[float, float]:
        """
        Bottom right coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.bottomright

    @bottomright.setter
    def bottomright(self, value: tuple[float, float]):
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
    def center(self) -> tuple[float, float]:
        """
        Center coordinate of bounding box.

        :getter: the coordinates
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.center

    @center.setter
    def center(self, value: tuple[float, float]):
        self._move(value[0] - self._rect.centerx, value[1] - self._rect.centery)

    @property
    def midtop(self) -> tuple[float, float]:
        """
        Center top coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midtop

    @midtop.setter
    def midtop(self, value: tuple[float, float]):
        self._move(value[0] - self._rect.centerx, value[1] - self._rect.y)

    @property
    def midright(self) -> tuple[float, float]:
        """
        Right center coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midright

    @midright.setter
    def midright(self, value: tuple[float, float]):
        self._move(value[0] - self.right, value[1] - self.centery)

    @property
    def midbottom(self) -> tuple[float, float]:
        """
        Center bottom coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midbottom

    @midbottom.setter
    def midbottom(self, value: tuple[float, float]):
        self._move(value[0] - self._rect.centerx, value[1] - self._rect.bottom)

    @property
    def midleft(self) -> tuple[float, float]:
        """
        Left center coordinate of bounding box.

        :getter: the coordinate
        :setter: the new coordinates
        :type: tuple(float/int, float/int)
        """
        return self._rect.midleft

    @midleft.setter
    def midleft(self, value: tuple[float, float]):
        self._move(value[0] - self._rect.left, value[1] - self._rect.centery)

    @property
    def size(self) -> tuple[float, float]:
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
