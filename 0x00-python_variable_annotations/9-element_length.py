#!/usr/bin/env python3

"""
contains a type annotated function
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    computes length of a list of sequences
    """
    return [(i, len(i)) for i in lst]
