N=int(input("enter a no of numbers"))
pos,neg,zero,even,odd=0,0,0,0,0
for i in range(N):
    num=int(input("enter any numbers"))
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
    if num%2==0:
        even+=1
    else:
        odd+=1
#display no. of each
print(pos,":no. of positive num ,",neg,":no. of negetive num,",zero,":no. of positive num")
print(even,":no. of even num,",odd,":no. of positive num")