#!/usr/bin/python3
'''MRU Caching'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''Most Recently used caching policy'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''add cache data'''
        if item is not None and key is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    mostUsedKey, _ = self.cache_data.popitem(False)
                    print(f'DISCARD: {mostUsedKey}')
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        '''retrieve cache data'''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
