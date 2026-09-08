Employee={}
n=int(input("Enter no. of Employee="))
for i in range(n):
    key=input("Enter Employee name=")
    value=float(input("Enter salary="))
    Employee[key]=value
high=max(Employee.values())
for t in Employee:
    if Employee[t]==high:
        print("Employee with highest salary is:",t,"with salary",high,"lpa")