"""Write a Python program to accept the N number of students and 
store each student's name, age and marks in a “student.txt” 
text file using the format operator. Display a message after 
successfully storing all student records.
"""
f=open("student.txt","w")
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Name of student: ")
    age=int(input("Age of student: "))
    marks=int(input(" Marks of student: "))
    f.write("%s %d %d\n"%(name,age,marks))
print("Sucessfully updated")
f.close()