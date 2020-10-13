from math import sqrt
from typing import Union, List, Tuple


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

    def __init__(self, x: Union[float, int], y: Union[float, int]):
        self._x = x
        self._y = y

    def __add__(self, other: "Vector2") -> "Vector2":
        x: Union[float, int] = self._x + other._x
        y: Union[float, int] = self._y + other._y
        return Vector2(x, y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        x: Union[float, int] = self._x - other._x
        y: Union[float, int] = self._y - other._y
        return Vector2(x, y)

    def __mul__(self, other: "Vector2") -> Union[float, int]:
        """Returns a dot product"""
        return self._x * other._x + self._y * other._y

    @property
    def x(self) -> Union[float, int]:
        """
        Return x component of the vector.

        :getter: a component value.
        :setter: a new component value.
        :type: float, int
        """
        return self._x

    @x.setter
    def x(self, value: Union[float, int]):
        self._x = value

    @property
    def y(self) -> Union[float, int]:
        """
        Return y component of the vector.

        :getter: a component value.
        :setter: a new component value.
        :type: float, int
        """
        return self._y

    @y.setter
    def y(self, value: Union[float, int]):
        self._y = value

    @property
    def xy(self) -> Tuple[Union[float, int]]:
        """
        Return x and y component of the vector as a tuple.

        :getter: a component value as a tuple.
        :setter: a new component value.
        :type: tuple(float/int, float/int)
        """
        return self._x, self._y

    @xy.setter
    def xy(self, value: Union[List[Union[float, int]], Tuple[Union[float, int]]]):
        self._x, self._y = value

    def normalize(self) -> "Vector2":
        """
        Normalizes vector (makes it as a unit vector)
        :return: Normalized vector
        :rtype: Vector2
        """
        norm = sqrt(self._x ** 2 + self._y ** 2)
        return Vector2(self._x / norm, self._y / norm)

    def normalize_ip(self) -> "Vector2":
        """
        Normalizes vector (makes it as a unit vector) in-place modifying
        this vector itself.

        :return: self
        :rtype: Vector2
        """
        norm = sqrt(self._x ** 2 + self._y ** 2)
        self._x /= norm
        self._y /= norm
        return self

    def __repr__(self):
        return f"Vector2<{self._x}, {self._y}>"

    def __str__(self):
        return f"Vector2({self._x}, {self._y})"
