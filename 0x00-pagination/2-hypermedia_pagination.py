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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pageWithBabyNames = self.dataset()
        try:
            (startIdx, endIdx) = index_range(page, page_size)
            return pageWithBabyNames[startIdx:endIdx]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''returns pagination details'''
        pageData = self.get_page(page, page_size)
        totalNumberOfPages = math.ceil(len(self.dataset()) / page_size)
        if page < totalNumberOfPages:
            nxtPage = page + 1
        else:
            nxtPage = None
        if page == 1:
            prevPage = None
        else:
            prevPage = page - 1
        pageObject = {
            'page_size': len(pageData),
            'page': page,
            'data': pageData,
            'next_page': nxtPage,
            'prev_page': prevPage,
            'total_pages': totalNumberOfPages,
        }
        return pageObject


def index_range(page: int, page_size: int) -> tuple:
    '''seek pagination function that returns a start & end index'''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
