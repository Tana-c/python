class Pet:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}"

    def makeSound(self):
        return f"{self.name} says "
