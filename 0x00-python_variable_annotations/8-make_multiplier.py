#!/usr/bin/env python3
"""
Module of a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
