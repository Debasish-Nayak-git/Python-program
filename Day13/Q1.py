avg=0
class Employee:
    def input1(self):
        emid=int(input("enter your employee id:"))
        name=input("enter your name: ")
        basic=int(input("Basic salary="))
        Hra=(20*basic)/100
        Da=(15*basic)/100
        Pf=(12*basic)/100
        gross_salary=basic+Hra+Da
        net_salary=gross_salary-Pf
        print("Name:",name,"\nEmid:",emid)
        print("net salary:",net_salary)
        print("gross salary:",gross_salary)
class Salary(Employee):
    pass
Emp=Salary()
Emp.input1()