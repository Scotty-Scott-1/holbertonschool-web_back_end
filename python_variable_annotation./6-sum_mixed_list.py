#!/usr/bin/env python3
"""a module with a function that returns the sum of a mixedlist"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a mixed list"""
    return sum(mxd_lst)
