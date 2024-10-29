from employee.person import Person


class Teacher(Person):
    def __init__(self, name, age, email, teacher_id):
        super().__init__(name, age, email)
        self.teacher_id = teacher_id

    def display_info(self):
        super().display_info()
        print(f"Teacher ID: {self.teacher_id}, Courses Teaching:")
