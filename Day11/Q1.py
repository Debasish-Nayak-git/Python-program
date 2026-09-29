"""	 Write a Python program using command-line arguments to 
accept a student's name, roll number, and marks in five subjects.
 Calculate the total, average, percentage, grade, and result
A student must score at least 40 marks in each subject to pass.
"""
import sys
print("Name:",sys.argv[1])
print("Roll Number:",sys.argv[2])
marks=[]
for i in range(3,len(sys.argv)):
    marks.append(int(sys.argv[i]))
print("Marks:",marks)
print("total:",sum(marks))
print("average:",sum(marks)/5)
print("percentage:",(sum(marks)/500)*100)
if all(m >= 40 for m in marks):
    print("Result: Pass")
else:
    print("Result: Fail")