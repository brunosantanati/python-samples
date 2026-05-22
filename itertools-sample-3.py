from itertools import groupby

# Notice how identical letters are grouped right next to each other
letters = ['A', 'A', 'B', 'B', 'B', 'A']

# groupby gives us pairs: (the item, a group of those items)
for key, group in groupby(letters):
    print(f"Letter: {key} -> Group items: {list(group)}")
    
print()
# Sorting makes sure all identical items are neighbors!
letters.sort()  # Now it becomes: ['A', 'A', 'A', 'B', 'B', 'B']

for key, group in groupby(letters):
    print(f"Letter: {key} -> Group items: {list(group)}")