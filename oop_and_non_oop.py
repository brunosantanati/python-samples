# 1. Class here
class Robot:
    def __init__(self, name):
        self.name = name

    # 2. Function inside the class (Instance Method)
    def greet_user(self):
        print(f"Hello, I am {self.name}!")


# 3. Function outside a class (Standalone Function)
def calculate_battery_percentage(voltage):
    # Just a simple math utility, no object state needed!
    return (voltage / 4.2) * 100


# --- execution starts here out in the open ---

# Create the object instance
my_robot = Robot("R2-D2")

# 4. Call obj.function
my_robot.greet_user()

# 5. Call outside-function
current_battery = calculate_battery_percentage(3.8)
print(f"System battery status: {current_battery:.1f}%")