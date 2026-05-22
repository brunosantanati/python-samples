numbers = [1, 2, 3, 4]

doubled = []

for x in numbers:
    doubled.append(x * 2)
    
print(doubled)

# List comprehension

numbers2 = [5, 6, 7, 8]

doubled2 = [x * 2 for x in numbers2]

print(doubled2)

# list comprehension with a condition

numbers3 = [-2, -1, 0, 1, 2]

positive = [x for x in numbers3 if x >= 0]

print(positive)