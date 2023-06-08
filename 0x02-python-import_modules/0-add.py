#!/usr/bin/python3

"""
This program imports the function `add` from the file `add_0.py`
and prints the result of the addition 1 + 2 = 3.
"""

if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
