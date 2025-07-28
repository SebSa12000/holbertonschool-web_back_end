#!/usr/bin/env python3
''' k v function '''


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' to_kv '''
    return (k, v * v)
