#!/usr/bin/env python3
"""
Module of a type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of integers and floats in a mixed list."""
    return sum(mxd_lst)


if __name__ == "__main__":
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans,
                                                                  type(ans)))
