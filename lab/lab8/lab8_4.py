class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email})"


person1 = Person("Thanachote chalermsuk", 22, "thanachote.ch@ksu.ac.th")
person2 = Person("Mr. TANA", 22, "herokoonchat@gmail.com")
print(person1)
print(person2)
