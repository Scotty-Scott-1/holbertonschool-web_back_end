#!/usr/bin/env python3
"""a module with a function that returns a tuple"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple where first element is arg: k
    and second arg: v squared"""

    second: float = v ** 2
    return k, second
