#!/usr/bin/env python3
"""a module with a function that returns a functione"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that returns a function"""
    def func(num: float) -> float:
        """returns an arg * multiplier"""
        return num * multiplier

    return func
