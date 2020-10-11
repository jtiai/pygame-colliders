from typing import Union

from .types import PairOrIntFloat


class Rect:
    """
    A rectangle to hold simple bounding rectangle around the colliders.

    :param x: x coordinate or tuple of (x,y) coordinates
    :param y: y coordinate or tuple of (width, height)
    :param w: width
    :param h: height
    :type x: int, float, tuple(int/float, int/float)
    :type y: int, float, tuple(int/float, int/float)
    :type w: float, int or None
    :type h: float, int or None
    """
    def __init__(
        self,
        x: PairOrIntFloat,
        y: PairOrIntFloat,
        w: Union[None, int, float] = None,
        h: Union[None, int, float] = None,
    ):
        if isinstance(x, tuple):
            self._x = x[0]
            self._y = x[1]
            if isinstance(y, tuple):
                self._w = y[0]
                self._h = y[1]
            else:
                raise TypeError("Parameters must be (x,y), (w,h) or x, y, w, h")
        else:
            self._x = x
            self._y = y
            self._w = w
            self._h = h

    @property
    def x(self) -> float:
        """
        x location (left) of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        """
        y location (top) of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    @property
    def w(self) -> float:
        """
        Width of the rect.

        :getter: the width
        :setter: the new width
        :type: float, int
        """
        return self._w

    @w.setter
    def w(self, value: float):
        self._w = value

    @property
    def h(self) -> float:
        """
        Height of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._h

    @h.setter
    def h(self, value: float):
        self._h = value

    @property
    def left(self) -> float:
        """
        Left location of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._x

    @left.setter
    def left(self, value: float):
        self._x = value

    @property
    def top(self) -> float:
        """
        Top location of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._y

    @top.setter
    def top(self, value: float):
        self._y = value

    @property
    def right(self) -> float:
        """
        Right location of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._x + self._w

    @right.setter
    def right(self, value: float):
        self._x = value - self._w

    @property
    def bottom(self) -> float:
        """
        Bottom location of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._y + self._h

    @bottom.setter
    def bottom(self, value: float):
        self._y = value - self._h

    @property
    def topleft(self) -> tuple[float, float]:
        """
        Top left location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y

    @topleft.setter
    def topleft(self, value: tuple[float, float]):
        self._x = value[0]
        self._y = value[1]

    @property
    def topright(self) -> tuple[float, float]:
        """
        Top right location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w, self._y

    @topright.setter
    def topright(self, value: tuple[float, float]):
        self._x = value[0] - self._w
        self._y = value[1]

    @property
    def bottomleft(self) -> tuple[float, float]:
        """
        Bottom left location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y + self._h

    @bottomleft.setter
    def bottomleft(self, value: tuple[float, float]):
        self._x = value[0]
        self._y = value[1] - self._h

    @property
    def bottomright(self) -> tuple[float, float]:
        """
        Bottom right location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w, self._y + self._h

    @bottomright.setter
    def bottomright(self, value: tuple[float, float]):
        self._x = value[0] - self._w
        self._y = value[1] - self._y

    @property
    def centerx(self) -> float:
        """
        Center x location of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._x + self._w / 2.0

    @centerx.setter
    def centerx(self, value: float):
        self._x = value - self._w / 2.0

    @property
    def centery(self) -> float:
        """
        Center y location of rect.

        :getter: the location
        :setter: the new location
        :type: float, int
        """
        return self._y + self._h / 2.0

    @centery.setter
    def centery(self, value: float):
        self._y = value - self._h / 2.0

    @property
    def center(self) -> tuple[float, float]:
        """
        Center location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w / 2.0, self._y + self._h / 2.0

    @center.setter
    def center(self, value: tuple[float, float]):
        self._x = value[0] - self._w / 2.0
        self._y = value[1] - self._h / 2.0

    @property
    def midtop(self) -> tuple[float, float]:
        """
        Mid top location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w / 2.0, self._y

    @midtop.setter
    def midtop(self, value: tuple[float, float]):
        self._x = value[0] - self._w / 2.0
        self._y = value[1]

    @property
    def midright(self) -> tuple[float, float]:
        """
        Mid right location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w, self.y + self._h / 2.0

    @midright.setter
    def midright(self, value: tuple[float, float]):
        self._x = value[0] - self._w
        self._y = value[1] - self._w / 2.0

    @property
    def midbottom(self) -> tuple[float, float]:
        """
        Mid bottom location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w / 2.0, self._y + self._h

    @midbottom.setter
    def midbottom(self, value: tuple[float, float]):
        self._x = value[0] - self._w / 2.0
        self._y = value[1] - self._h

    @property
    def midleft(self) -> tuple[float, float]:
        """
        Mid left location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y + self._h / 2.0

    @midleft.setter
    def midleft(self, value: tuple[float, float]):
        self._x = value[0]
        self._y = value[1] - self._h / 2.0

    @property
    def size(self) -> tuple[float, float]:
        """
        Size of rect.

        :getter: the size
        :setter: the new size
        :type: tuple(float/int, float/int)
        """
        return self._w, self._h

    @size.setter
    def size(self, value: tuple[float, float]):
        self._w = value[0]
        self._h = value[1]

    @property
    def width(self) -> float:
        """
        Width of rect.

        :getter: the width
        :setter: the new width
        :type: float, int
        """
        return self._w

    @width.setter
    def width(self, value: float):
        self._w = value

    @property
    def height(self) -> float:
        """
        Height of rect.

        :getter: the height
        :setter: the new height
        :type: float, int
        """
        return self._h

    @height.setter
    def height(self, value: float):
        self._h = value
