"""
*args

Collects extra positional arguments into a tuple.
“Take all extra positional arguments and pack them together.”
"""

def add(*numbers):
    print(numbers)

add(1, 2, 3)