#!/usr/bin/python3
'''LIFO caching'''
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO caching'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''add cache data'''
        if item is not None and key is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    # getting the key to the last item in cache dict
                    lastCacheKey = list(self.cache_data.keys())[-1]
                    # discarding the last item
                    del self.cache_data[lastCacheKey]
                    print(f'DISCARD: {lastCacheKey}')

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''retrieve cache data'''
        if key is None or not key:
            return None
        return self.cache_data.get(key)
