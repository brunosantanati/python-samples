"""
**kwargs

Collects keyword arguments into a dictionary.
“Take all named arguments and pack them into a dictionary.”
"""

def show_user(**data):
    print(data)

show_user(name="Bruno", age=20)