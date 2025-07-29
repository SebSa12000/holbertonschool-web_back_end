#!/usr/bin/env python3
'''Element length'''


from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Element length'''
    return [(i, len(i)) for i in lst]