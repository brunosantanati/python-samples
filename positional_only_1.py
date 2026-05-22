def greet(name, /):
    print(name)
    
# Allowed:
greet("Bruno")

# Not allowed:
# greet(name="Bruno")