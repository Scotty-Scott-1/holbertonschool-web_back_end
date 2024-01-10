#!/usr/bin/env python3
"""a module that gets the requried pages of the dataset"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple with start and end index"""
    start = (page - 1) * page_size
    end = page * page_size
    result = (start, end)
    return result


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """check the args and return the list of lists(dataset lines)"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(data) or end <= 0:
            return []

        return data[start:end]
