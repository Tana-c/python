class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_status = "Raw"
        self.condiments = []

    def cook(self, time):
        self.cooked_level += time

        if self.cooked_level > 0 and self.cooked_level <= 3:
            self.cooked_status = "Raw"
        elif self.cooked_level > 3 and self.cooked_level <= 6:
            self.cooked_status = "Medium"
        elif self.cooked_level > 6 and self.cooked_level <= 9:
            self.cooked_status = "Well-done"
        else:
            self.cooked_status = "Charcoal"

    def addCodiment(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        if self.condiments:
            return f"{self.cooked_status} hot_dog with {', '.join(self.condiments)}."
        else:
            return f"{self.cooked_status} hot_dog."


myDog = HotDog()
print(myDog)

print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)

print("Cooking hot dog for 3 minutes...")
myDog.cook(3)
print(myDog)

print("Cooking hot dog for 10 minutes...")
myDog.cook(10)
print(myDog)

myDog.addCodiment("ketchup")
myDog.addCodiment("mustard")
print(myDog)
