import sys

def get_huge_dataset_generator():
    for i in range(10_000_000):
        yield i * 2  #  Hands over ONE number, pauses, and remembers its spot!

numbers_gen = get_huge_dataset_generator() # it's a generator object.
# Let's check how much RAM this generator object uses:
print(f"Generator memory: {sys.getsizeof(numbers_gen)} bytes")
# Output: Generator memory: 208 bytes (!!!)


#print(numbers_gen)
#print(type(numbers_gen))
#for x in numbers_gen:
#    print(x)