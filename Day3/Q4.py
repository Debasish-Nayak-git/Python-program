n=int(input("enter no. of empolyees:"))
avg=0.0
for i in range(n):
    emid=int(input("enter your employee id:"))
    name=input("enter your name: ")
    basic=int(input("Basic salary="))
    Hra=(20*basic)/100
    Da=(15*basic)/100
    Pf=(12*basic)/100
    gross_salary=basic+Hra+Da
    net_salary=gross_salary-Pf
    if net_salary>80000:
        print("name:",name," em_id:",emid)
        print("salary:",net_salary)
        print("A grade")
    elif net_salary>60000:
        print("name:",name," em_id:",emid)
        print("salary:",net_salary)
        print("B grade")
    elif net_salary>40000:
        print("name:",name," em_id:",emid)
        print("salary:",net_salary)
        print("C grade")
    else:
        print("name:",name," em_id:",emid)
        print("salary:",net_salary)
        print("D grade")
    avg+=net_salary
print("total employees:",n)
print("Average salary:",(avg/n))