"""
Normal function

def numbers():
    return [1, 2, 3]
"""

# Generator

def numbers():
    yield 1
    yield 2
    yield 3
    
for n in numbers():
    print(n)