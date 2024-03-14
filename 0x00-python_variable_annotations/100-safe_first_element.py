#!/usr/bin/env python3
"""code with the correct duck-typed annotations"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ correct duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
