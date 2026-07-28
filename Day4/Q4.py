floor=int(input("Enter no. of floor:"))
room=int(input ("enter no of rooms in each floor:"))
hotel=[]
for i in range(1,floor+1):
    print("floor:",i+1)
    row=[]
    for j in range(room):
        status=input("Enter room status(A for avialable,B for Booked):")
        if status=="A" or status=="B":
            row.append(status)
        else:
            print("wrong input!")
            row.append("A")
    hotel.append(row)
print("hotel room status:")
for i in range (floor,0,-1):
    print("floor",i,":",end=" ")
    for j in range(room):
        print(hotel[i-1][j],end=" ")
    print()
