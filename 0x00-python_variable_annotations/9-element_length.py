#!/usr/bin/env python3

"""
contains a type annotated function
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    ducktyping an iterable object
    """
    return [(i, len(i)) for i in lst]