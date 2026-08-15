#student result system
name=input("name=")
reg=int(input("reg="))
marks=eval(input("marks of three subject:"))
res=lambda a:sum(a)
per=lambda a:(sum(a)/len(a))
grd=lambda a:("O" if a>=90 else "E" if a>=80 else
              "A" if a>=70 else "B" if a>=60 else
              "C" if a>=50 else "F")
print("total marks:",res(marks))
print("percentage marks:",per(marks))
if grd(per(marks))=="F":
    print("fail")
else:
    print(grd(per(marks))," grade")