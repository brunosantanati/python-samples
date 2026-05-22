from collections import deque

# 1. Initialize an empty queue
ticket_queue = deque()

# 2. Customers line up (Enqueuing / Appending to the right)
print("--- Customers entering the queue ---")
ticket_queue.append("Alice (Ticket #101)")
ticket_queue.append("Bob (Ticket #102)")
ticket_queue.append("Charlie (Ticket #103)")
print(f"Current Queue: {list(ticket_queue)}\n")

# 3. Serving customers in order (Dequeuing / Popping from the left)
print("--- Serving customers (FIFO) ---")
while len(ticket_queue) > 0:
    # .popleft() removes and returns the first item
    next_customer = ticket_queue.popleft()
    print(f"Now serving: {next_customer}")
    print(f"Remaining in line: {list(ticket_queue)}")

print("\nAll customers have been served!")