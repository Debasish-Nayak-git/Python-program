"""
Q3. Write a Python program to create a Student class 
with name, rollnumber, course and marks as attributes. 
Use self and methods to accept details, calculate total and 
average marks and display the result using user input.
"""
class Student:
    def display(self,name,roll,course,marks):
        print("Name:",name)
        print("Roll Number:",roll)
        print("Course:",course)
        print("Marks:",marks)
        print("Total Marks:",sum(marks))
        print("Average Marks:",sum(marks)/len(marks))
s=Student()
name=input("Enter Name:")
roll=int(input("Enter Roll Number:"))
course=input("Enter Course:")
marks=eval(input("Enter Marks:"))
s.display(name,roll,course,marks)