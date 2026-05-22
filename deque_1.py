from collections import deque

# A deque is like a super list optimized for adding/removing from BOTH ends.
# Normal lists are slow when removing from the front.
# deque is fast.
# Useful for:
# - queues
# - undo systems
# - browser history

dq = deque([1, 2, 3])

dq.appendleft(0)
dq.append(4)

print(dq)