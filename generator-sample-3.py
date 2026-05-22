def read_massive_log(file_path):
    # This keeps only ONE line in memory at any given second
    with open(file_path, "r") as file:
        for line in file:
            if "def" in line:
                yield line.strip()

# Using the stream generator
# It pulls a line from the hard drive, processes it, drops it, and moves on.
for error_line in read_massive_log("generator-sample-1.py"):
    print(f"Found a function: {error_line}")
    # If we find what we want, we can break out early. 
    # We never wasted time or RAM loading the rest of the 50GB file!
    break