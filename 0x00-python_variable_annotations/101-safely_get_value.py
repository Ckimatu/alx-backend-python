#!/usr/bin/env python3

"""
contains type annotated function
"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: T,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    adding annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
