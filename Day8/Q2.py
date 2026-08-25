l=[20,30,45]
remove=lambda a:l.remove(a) if a in l else print("value not found")
search=lambda a:"found" if a in l else "not found"
while(True):
    print("1.append")
    print("2.insert")
    print("3.remove")
    print("4.pop")
    print("5.search")
    print("6.sort")
    print("7.Reverse")
    print("8.Display")
    print("9.Exit")
    ch=int(input("Enter your choice:"))
    if ch==9:
        print("succefully exit!")
        break
    elif ch==8:
        print(l)
    elif ch==7:
        l.sort(reverse=True)
    elif ch==6:
        l.sort()
    elif ch==5:
        a=int(input("value to search="))
        print(a,search(a))
    elif ch==4:
        l.pop()
    elif ch==3:
        print(l)
        a=int(input("value="))
        remove(a)
    elif ch==2:
        a=int(input("value="))
        a1=int(input("index="))
        l.insert(a1,a)
    elif ch==1:
        a=int(input("value="))
        l.append(a)
    else:
        print("Wrong choice!")