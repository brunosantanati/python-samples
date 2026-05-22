from itertools import groupby

# Remember to sort the list first so identical items are neighbors!
letters = ['A', 'A', 'B', 'B', 'B', 'A']
letters.sort()  # ['A', 'A', 'A', 'B', 'B', 'B']

# 1. Initialize an empty dictionary
grouped_dict = {}

# 2. Loop through groupby and save to the dict
for key, group in groupby(letters):
    # CRUCIAL: You must wrap 'group' in list() before saving it,
    # otherwise Python will empty out the generator object!
    grouped_dict[key] = list(group)

print(grouped_dict)