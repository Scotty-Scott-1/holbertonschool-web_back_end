#!/usr/bin/env python3
"""a module with a function that takes list or tuple containing sequence types
and returns a list of tuples(element 1: the sequance, element 2: len )"""


from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a module with a function
    that takes list or tuple containing sequence types
    and returns a list of tuples(element 1: the sequance, element 2: len )"""
    return [(i, len(i)) for i in lst]
