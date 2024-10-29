from employee.student import Student
from employee.teacher import Teacher

university = [
    Teacher("Dr. tana", 22, "ta@university.com", "T001"),
    Teacher("Prof. Johnson", 50, "johnson@university.com", "T002"),
    Teacher("Ms. Davis", 38, "davis@university.com", "T003"),
    Student("wewl", 20, "wewl@student.com", "S001"),
    Student("rat", 22, "rat@student.com", "S002"),
    Student("cacel", 19, "cacel@student.com", "S003"),
]

for i, person in enumerate(university):
    print(i + 1, end=". ")
    person.display_info()
    print("----------")
