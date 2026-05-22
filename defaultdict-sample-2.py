from collections import defaultdict

"""
Accumulating Totals (defaultdict(int))
If you pass int as the factory, the default value for any new key becomes 0 (because calling int() in Python returns 0).
This makes it great for tracking scores or custom counting.
"""

scores = defaultdict(int)

# We can add points directly, even though "Player 1" doesn't exist yet!
scores["Player 1"] += 10  # 0 + 10 = 10
scores["Player 2"] += 5   # 0 + 5 = 5
scores["Player 1"] += 15  # 10 + 15 = 25

print(dict(scores))
# Output: {'Player 1': 25, 'Player 2': 5}