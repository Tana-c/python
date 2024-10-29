from employee.person import Person


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} has been enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def display_courses(self):
        if self.courses:
            print(f"{self.name}'s Courses: {', '.join(self.courses)}")

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        self.display_courses()
