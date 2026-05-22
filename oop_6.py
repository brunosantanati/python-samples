class SmartLight:
    def __init__(self):
        self.is_on = False
        self.brightness = 0  # percentage 0-100

    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        print("Light turned ON at full brightness.")

    def dim_to(self, level):
        # We use self to check the status variable set by other methods
        if not self.is_on:
            # We use self to call another method inside this class!
            self.turn_on() 
            
        self.brightness = level
        print(f"Light adjusted to {self.brightness}%.")

    def status_report(self):
        # Reading multiple variables managed by the other methods
        state = "ON" if self.is_on else "OFF"
        print(f"[REPORT] Power: {state} | Brightness: {self.brightness}%")

# --- Let's test our multi-method class ---
living_room_light = SmartLight()

# We call them cleanly without passing 'self' manually
living_room_light.dim_to(40)     # Automatically turns on first, then dims
living_room_light.status_report() # Prints: [REPORT] Power: ON | Brightness: 40%