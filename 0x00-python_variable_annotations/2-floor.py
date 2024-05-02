#!/usr/bin/env python3
"""
Module for a type-annotated function floor
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of the float
    """
    return math.floor(n)


if __name__ == "__main__":
    ans = floor(3.14)
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
