#!/usr/bin/env python3
'''Simple pagination'''
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''returns a page's data'''
        assert isinstance(page, int) & page > 0
        assert isinstance(page_size, int) & page_size > 0
        (startIdx, endIdx) = index_range(page, page_size)
        pageBabyNamesData = self.dataset()
        if startIdx > len(pageBabyNamesData) | endIdx > len(pageBabyNamesData):
            return []
        return pageBabyNamesData[startIdx:endIdx]


def index_range(page: int, page_size: int) -> tuple:
    '''seek pagination function that returns a start & end index'''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
