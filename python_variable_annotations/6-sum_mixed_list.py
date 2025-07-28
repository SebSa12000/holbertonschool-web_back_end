#!/usr/bin/env python3
'''Sum mixed floats / int '''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Sum mixed floats / int '''
    sum = 0
    for item in mxd_lst:
        sum = sum + item
    return sum
