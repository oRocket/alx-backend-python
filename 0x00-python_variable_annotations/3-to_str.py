#!/usr/bin/env python3
"""
Module of a type-annotated function to_str
"""
def to_str(n: float) -> str:
    """Converts a float to its string representation."""
    return str(n)

if __name__ == "__main__":
    # Test the to_str function
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))  # Check if the result is the same as using str()
    print(to_str.__annotations__)  # Print the type annotations of the function
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))  # Print the result and its type
