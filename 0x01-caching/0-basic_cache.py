#!/usr/bin/python3
'''Basic dictionary'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''caching system basic cache class'''

    def put(self, key, item):
        '''add cache data'''
        if item is not None and key is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''retrieve cache data'''
        if key is None or not key:
            return None
        return self.cache_data.get(key)
