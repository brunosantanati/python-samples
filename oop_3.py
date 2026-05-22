class SecretAgent:
    def __init__(self, codename, real_name):
        self.codename = codename
        self.real_name = real_name

    def __getitem__(self, key):
        if key == "clearance_level":
            return "Top Secret"
        if key == "identity":
            return self.real_name
        return "ACCESS DENIED"

agent = SecretAgent(codename="007", real_name="James Bond")

# Look how natural it feels to access data using bracket keys:
print(agent["identity"])         # Output: James Bond
print(agent["clearance_level"]) # Output: Top Secret
print(agent["bank_account"])    # Output: ACCESS DENIED