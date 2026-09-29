"""
Q2. Write a Python program to create a Student class with
 name, age, and marks. Create two objects, assign values and 
 display their details.
"""
class Student:
    def display(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
S1=Student()
S1.display("Ashu",20,90)
S2=Student()
S2.display("Ravi",21,85)