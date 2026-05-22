from functools import lru_cache

# @lru_cache memoizes function results to avoid repeated expensive calculations.

@lru_cache
def slow_square(n):
    print("Calculating...")
    return n * n

print(slow_square(4))
print(slow_square(4))


# Output:

# Calculating...

# Only once.

# Second call uses cached result.