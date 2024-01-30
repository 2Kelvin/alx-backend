#!/usr/bin/python3
'''FIFO caching'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching class'''

    def put(self, key, item):
        '''add cache data'''
        if item is not None and key is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # getting the key to the 1st item in cache dict
            firstCacheKey = list(self.cache_data.keys())[0]
            # discard the first item
            del self.cache_data[firstCacheKey]
            print(f'DISCARD: {firstCacheKey}\n')

    def get(self, key):
        '''retrieve cache data'''
        if key is None or not key:
            return None
        return self.cache_data.get(key)
