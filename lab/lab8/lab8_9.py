from employee.student import Student

student1 = Student("jonny walker", 20, "jonny.wa@example.com", "S123456")
student1.display_info()
student1.enroll_course("Mathematics")
student1.enroll_course("Physics")
student1.display_courses()
student1.update_email("jonny.wa@university.com")
print()
student1.display_info()
