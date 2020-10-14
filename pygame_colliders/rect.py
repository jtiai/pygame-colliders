from typing import Union, List, Tuple


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
        x: Union[List[float], float],
        y: Union[List[float], float],
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
    def topleft(self) -> Tuple[float]:
        """
        Top left location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y

    @topleft.setter
    def topleft(self, value: Tuple[float]):
        self._x = value[0]
        self._y = value[1]

    @property
    def topright(self) -> Tuple[float]:
        """
        Top right location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w, self._y

    @topright.setter
    def topright(self, value: Tuple[float]):
        self._x = value[0] - self._w
        self._y = value[1]

    @property
    def bottomleft(self) -> Tuple[float]:
        """
        Bottom left location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y + self._h

    @bottomleft.setter
    def bottomleft(self, value: Tuple[float]):
        self._x = value[0]
        self._y = value[1] - self._h

    @property
    def bottomright(self) -> Tuple[float]:
        """
        Bottom right location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w, self._y + self._h

    @bottomright.setter
    def bottomright(self, value: Tuple[float]):
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
    def center(self) -> Tuple[float]:
        """
        Center location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w / 2.0, self._y + self._h / 2.0

    @center.setter
    def center(self, value: Tuple[float]):
        self._x = value[0] - self._w / 2.0
        self._y = value[1] - self._h / 2.0

    @property
    def midtop(self) -> Tuple[float]:
        """
        Mid top location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w / 2.0, self._y

    @midtop.setter
    def midtop(self, value: Tuple[float]):
        self._x = value[0] - self._w / 2.0
        self._y = value[1]

    @property
    def midright(self) -> Tuple[float]:
        """
        Mid right location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w, self.y + self._h / 2.0

    @midright.setter
    def midright(self, value: Tuple[float]):
        self._x = value[0] - self._w
        self._y = value[1] - self._w / 2.0

    @property
    def midbottom(self) -> Tuple[float]:
        """
        Mid bottom location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x + self._w / 2.0, self._y + self._h

    @midbottom.setter
    def midbottom(self, value: Tuple[float]):
        self._x = value[0] - self._w / 2.0
        self._y = value[1] - self._h

    @property
    def midleft(self) -> Tuple[float]:
        """
        Mid left location of rect.

        :getter: the location
        :setter: the new location
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y + self._h / 2.0

    @midleft.setter
    def midleft(self, value: Tuple[float]):
        self._x = value[0]
        self._y = value[1] - self._h / 2.0

    @property
    def size(self) -> Tuple[float]:
        """
        Size of rect.

        :getter: the size
        :setter: the new size
        :type: tuple(float/int, float/int)
        """
        return self._w, self._h

    @size.setter
    def size(self, value: Tuple[float]):
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

    def collide_rect(self, other: "Rect") -> bool:
        """
        Check if current rect collides with other rect
        :param other: Other rect to test
        :type other: Rect
        :return: True if collides, False otherwise
        :rtype: bool
        """
        # A.left < B.right and
        # A.top < A.bottom and
        # A.right > B.left and
        # A.bottom > b.top

        return (
            min(self._x, self._x + self._w) < max(other._x, other._x + other._w)
            and min(self._y, self._y + self._h) < max(other._y, other._y + other._h)
            and max(self._x, self._x + self._w) > min(other._x, other._x + other._w)
            and max(self._y, self._y + self._h) > min(other._y, other._y + other._h)
        )
