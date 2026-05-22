class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")
        
    def __str__(self):
        return f"Dog object: {self.name}"
    
    def __len__(self):
        return len(self.name)
        
dog = Dog("Rex")
print(dog)
print(len(dog))
print(dog.name)
dog.bark()

print()

dog2 = Dog("Glindo")
print(dog2)
print(len(dog2))