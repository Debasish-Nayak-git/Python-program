"""
Q1. Write a Python program to create an 
Employee class with name, salary and department.
 Create an object and display the details.
"""
class Employee:
    def details(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
E=Employee()
E.details("Ashu", 50000, "IT")