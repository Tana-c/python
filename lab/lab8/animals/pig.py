from animals.pet import Pet

class Pig(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def makeSound(self):
        return super().makeSound() + "Oink!"