def add(*numbers):
    total = 0

    for n in numbers:
        total += n

    return total

print(add(1, 2, 3, 4))