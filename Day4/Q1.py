#prime number
item=0
num=int(input("Enter the number:"))
for i in range(1,num):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
        item+=1
print("Number of prime numbers=",item)