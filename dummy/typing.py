"""Defines some custom type annotations."""

from typing import TypeAlias

from nptyping import Float64, NDArray, Shape


# noinspection PyUnresolvedReferences
NDSquareMatrix: TypeAlias = NDArray[Shape["Size, Size"], Float64]  # noqa: F821
"""Shorthand annotation for NumPy square matrix of floats.

Group
-----
    Functions
"""
