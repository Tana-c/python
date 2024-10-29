from employee.person import Person

class Employee(Person):
    def __init__(self, name, age, email, salary):
        super().__init__(name, age, email)
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to: {self.salary}")

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}")
