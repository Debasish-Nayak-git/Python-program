#perfect number
num=int(input("Range of loop:"))
count=0
for i in range(1,num+1):
    temp,total=i,0
    for j in range(1,i):
        if i%j==0:
            total=total+j
    if total==i:
        print(i,end=",")
        count+=1
print("\nnumber of perfect number in between 10 to ",num,"=",count)
