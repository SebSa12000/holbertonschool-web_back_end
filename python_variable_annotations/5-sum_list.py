#!/usr/bin/env python3
'''Sum floats'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' sum floats '''
    sum = 0
    for item in input_list:
        sum = sum + item
    return sum
