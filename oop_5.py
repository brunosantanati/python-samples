class CallCounter:
    def __init__(self, function_name):
        self.function_name = function_name
        self.count = 0  # 🧠 The object remembers this state!

    def __call__(self):
        self.count += 1
        print(f"Function '{self.function_name}' has been executed {self.count} times.")

# Create the callable object
logger = CallCounter("DatabaseSync")

# Call it like a function multiple times
logger()  # Output: Function 'DatabaseSync' has been executed 1 times.
logger()  # Output: Function 'DatabaseSync' has been executed 2 times.
logger()  # Output: Function 'DatabaseSync' has been executed 3 times.