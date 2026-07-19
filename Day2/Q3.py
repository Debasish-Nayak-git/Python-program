basic=int(input("Basic salary="))
Hra=(20*basic)/100
Da=(15*basic)/100
Pf=(12*basic)/100
gross_salary=basic+Hra+Da
net_salary=gross_salary-Pf
print("gross_salary",gross_salary)
print("net_salary",net_salary)
print("Hra=",Hra)
print("Da=",Da)
print("Pf=",Pf)
if net_salary>50000:
    print("Employee earn more than 50000")
else:
    print("Employee earn less than 50000")