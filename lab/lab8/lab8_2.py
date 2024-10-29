class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.email = ""

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")


person = Person()
person.name = "Thanachote chalermsuk"
person.age = 22
person.email = "thanachote.ch@ksu.ac.th"
person.display()
