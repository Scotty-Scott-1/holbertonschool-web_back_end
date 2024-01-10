#!/usr/bin/env python3
"""a module with a helper function"""


def index_range(page, page_size):
    """return a tuple with start and end index"""
    start = (page - 1) * page_size
    end = page * page_size
    result = (start, end)
    return result
