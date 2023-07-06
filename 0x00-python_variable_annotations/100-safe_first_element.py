#!/usr/bin/env python3

"""
contains an annotated function
"""
from typing import Sequence, Any, Union, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists
    """
    if lst:
        return lst[0]
    else:
        return None
