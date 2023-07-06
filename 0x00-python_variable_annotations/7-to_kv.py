#!/usr/bin/env python3

"""
contains a type-annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
     takes a string k and an int OR float v as argument
     and returns a tuple. First element of tuple is string k.
     The second element is the square of int/float v
     and should be annotated as a float.
    """
    return (k, v**2)
