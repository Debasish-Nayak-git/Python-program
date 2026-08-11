name=eval(input("ente name of three student:"))
mark=[]
for i in range(3):
    a=eval(input("Student marks in list:"))
    mark.append(a)
total=lambda a:sum(a)
avg=lambda a:(sum(a)/3)
high=lambda a:max(a)
low=lambda a:min(a)
for i in range (3):
    print("name=",name[i])
    print("total mark=",total(mark[i]),"\n avg=",avg(mark[i]))
    print("highest mark=",high(mark[i]),"\n lowest mark=",low(mark[i]))