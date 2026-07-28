row=int(input("Enter no. of rows:"))
for i in range(row+1):
    for j in range(row-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")  
    print()