from animals.cat import Cat
from animals.dog import Dog

# สร้างวัตถุ Dog
dog1 = Dog("LLL", "Golden Retriever", 3)
print(dog1.display_info())
print(dog1.makeSound())

# สร้างวัตถุ Cat
cat1 = Cat("jonny wallker", "Siamese", 2)
print(cat1.display_info())
print(cat1.makeSound())
