import time

def infinite_id_generator():
    current_id = 1
    while True:  # A loop that literally never ends!
        yield f"TXN-{current_id:06d}"
        current_id += 1

# Activate the infinite stream
id_stream = infinite_id_generator()

# We can request IDs forever using the built-in next() function
print(next(id_stream))  # Output: TXN-000001
print(next(id_stream))  # Output: TXN-000002

# We can simulate transactions coming in over time
for _ in range(3):
    time.sleep(0.5) # Pretend time is passing
    print(f"New transaction processed: {next(id_stream)}")