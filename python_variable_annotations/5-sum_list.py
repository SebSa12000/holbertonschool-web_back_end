#!/usr/bin/env python3
'''Sum floats'''


def add(input_list: list[float]) -> float:
    ''' sum floats '''
    sum = 0
    for item in input_list:
        sum = sum + item
    return sum
