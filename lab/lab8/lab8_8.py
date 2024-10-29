from employee.employee import Employee

employee1 = Employee("Jonny walker", 45, "jonny.wa@example.com", 45000)
employee1.display_info()
employee1.update_email("jonny.wa@newdomain.com")
employee1.update_salary(50000)
employee1.display_info()
