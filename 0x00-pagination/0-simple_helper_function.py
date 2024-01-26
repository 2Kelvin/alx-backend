#!/usr/bin/env python3
'''Simple helper function'''


def index_range(page: int, page_size: int) -> tuple:
    '''seek pagination function that returns a start & end index'''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
