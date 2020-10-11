from typing import Union, List

from .types import FloatOrInt

class Vector2:
    """
    A class to handle 2 dimensional vector operations.

    Example of usage:

    .. code-block:: python

        vec_a = Vector2(12.1, 23.4)
        vec_b = Vector2(2.5, 11.73)
        vec_c = vec_b - vec_a

    :param x: x component of the vector
    :param y: y component of the vector
    :type x: float, int
    :type y: float, int
    """
    def __init__(self, x: FloatOrInt, y: FloatOrInt):
        self._x = x
        self._y = y

    def __add__(self, other: "Vector2") -> "Vector2":
        x: FloatOrInt = self._x + other._x
        y: FloatOrInt = self._y + other._y
        return Vector2(x, y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        x: FloatOrInt = self._x - other._x
        y: FloatOrInt = self._y - other._y
        return Vector2(x, y)

    def __mul__(self, other: "Vector2") -> FloatOrInt:
        """Returns a dot product"""
        return self._x * other._x + self._y * other._y

    @property
    def x(self) -> FloatOrInt:
        """
        Return x component of the vector.

        :getter: a component value.
        :setter: a new component value.
        :type: float, int
        """
        return self._x

    @x.setter
    def x(self, value: FloatOrInt):
        self._x = value

    @property
    def y(self) -> FloatOrInt:
        """
        Return y component of the vector.

        :getter: a component value.
        :setter: a new component value.
        :type: float, int
        """
        return self._y

    @y.setter
    def y(self, value: FloatOrInt):
        self._y = value

    @property
    def xy(self) -> tuple[FloatOrInt, FloatOrInt]:
        """
        Return x and y component of the vector as a tuple.

        :getter: a component value as a tuple.
        :setter: a new component value.
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y

    @xy.setter
    def xy(self, value: Union[List[FloatOrInt], tuple[FloatOrInt, FloatOrInt]]):
        self._x, self._y = value
