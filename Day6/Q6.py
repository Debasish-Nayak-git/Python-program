#student result system
name=input("name=")
reg=int(input("reg="))
marks=eval(input("marks of three subject:"))
res=lambda a:sum(a)
per=lambda a:(sum(a)/3)
def grd(a):
    if a>=90:
        return "O"
    elif a>=80:
        return "E"
    elif a>=70:
        return "A"
    elif a>=60:
        return "B"
    elif a>=50:
        return "C"
    else:
        return "F"
print("total marks:",res(marks))
print("percentage marks:",per(marks))
if grd(per(marks))=="F":
    print("fail")
else:
    print(grd(per(marks))," grade")