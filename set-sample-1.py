# Sets store unique values only.
# Sets are mutable.
# Sets are unordered.
# To modify a set you usually:
# - remove the old value
# - add the new value

numbers = {1, 2, 2, 3, 3, 3}

print(numbers) # No duplicates

numbers.add(20)

print(numbers)

numbers.remove(1)

print(numbers)

# checking membership quickly. This should be faster than using it with lists or tuples
if 20 in numbers:
    print("Found!")
    print("Hurray!")