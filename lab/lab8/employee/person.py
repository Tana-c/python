class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"{self.name}'s email has been updated to: {self.email}")
