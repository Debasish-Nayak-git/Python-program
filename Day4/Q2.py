#armstrong number
num=int(input("Enter a number>10:"))
count=0
for i in range(10,num+1):
    temp,arm=i,0
    digits=len(str(i))
    while temp>0:
        digit=temp%10
        arm=arm+(digit**digits)
        temp=temp//10
    if arm==i:
        print(i,end=",")
        count+=1
print("\nnumber of armstrong number in between 10 to ",num,"=",count)
