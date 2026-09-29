"""Write a Python program using command-line arguments to accept 
an employee's name, ID, and five performance scores. Calculate 
the total and average scores, assign a grade, and display the 
performance report.
"""
import sys
print("Name:",sys.argv[1])
print("Id:",sys.argv[2])
prform=[]
for i in range(3,len(sys.argv)):
    prform.append(int(sys.argv[i]))
print("total:",sum(prform))
print("average:",sum(prform)/5)
r=lambda x: "A" if x >= 80 else "B" if x >= 60 else "C"
print("Grade:",r(sum(prform)/5))