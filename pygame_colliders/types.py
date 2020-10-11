from typing import Union, List

FloatOrInt = Union[float, int]
PairOrFloat = Union[float, Union[List[float], tuple[float, float]]]
PairOrIntFloat = Union[Union[int, float], Union[List[Union[int, float]], Union[tuple[int, int], tuple[float, float]]]]
