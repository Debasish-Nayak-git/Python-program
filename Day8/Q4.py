l=[10,20,30,25,35,55]
t=tuple(l)
search=lambda a:"found" if a in l else "not found"
while True:
    print("1.index")
    print("2.slice")
    print("3.max")
    print("4.min")
    print("5.count")
    print("6.search")
    print("7.Exit")
    ch=int(input("Enter your choice:"))
    if ch==7:
        break
    elif ch==1:
        i=int(input("index ="))
        if 0<=i and i<len(t):
            print(t[i])
        else:
            print("index out of bound")
    elif ch==2:
        print(t[1:3])
    elif ch==3:
        print("maximum:",max(t))
    elif ch==4:
        print("minimu:",min(t))
    elif ch==5:
        print("count=",len(t))
    elif ch==6:
        v=int(input("Value="))
        print(v," ",search(v))
    else:
        print("wrong choice!")
