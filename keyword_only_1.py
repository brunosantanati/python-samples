# Keyword-only (*)

def greet(*, name):
    print(name)

# Allowed:

greet(name="Bruno")

# Not allowed:

#greet("Bruno")