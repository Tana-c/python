from animals.cat import Cat
from animals.dog import Dog
from animals.pig import Pig

cat1 = Cat("jonny", "Siamese", 2)
cat2 = Cat("sunee", "Persian", 4)
cat3 = Cat("dumdum", "British Shorthair", 3)

dog1 = Dog("heangheang", "Golden Retriever", 3)
dog2 = Dog("TAKTAK", "Beagle", 5)
dog3 = Dog("LL", "German Shepherd", 2)

pig1 = Pig("Piggy1", "Pig", 1)
pig2 = Pig("Piggy2", "Pig", 3)
pig3 = Pig("Piggy3", "Pig", 5)

pets = [cat1, dog1, cat2, dog2, cat3, dog3, pig1, pig2, pig3]

for i in range(len(pets)):
    pet = pets[i]
    print(f"{i+1}. {pet.makeSound()}")
