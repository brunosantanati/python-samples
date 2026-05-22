from collections import defaultdict

# Grouping Items (defaultdict(list))

data = [
    ("Math", "Alice"),
    ("Science", "Bob"),
    ("Math", "Charlie"),
    ("Science", "David")
]

# Tell it to automatically create an empty list [] for any new key
classroom = defaultdict(list)

for subject, student in data:
    # If 'subject' isn't in the dict, Python instantly creates it as []
    # and then immediately appends the student to it.
    classroom[subject].append(student)

print(dict(classroom))
# Output: {'Math': ['Alice', 'Charlie'], 'Science': ['Bob', 'David']}