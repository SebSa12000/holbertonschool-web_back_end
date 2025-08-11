#!/usr/bin/env python3
"""
Helper function
"""


def index_range(page, page_size):
    ''' return the page size '''
    return ((page - 1)*page_size, page * page_size)
