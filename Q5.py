n=eval(input("enter 5 numbers in format [1,2,..]"))
big=0
if n[4]>=n[3] and n[4]>=n[2] and n[4]>=n[1] and n[4]>=n[0]:
    big=n[4] 
elif n[3]>=n[4] and n[3]>=n[2] and n[3]>=n[1] and n[3]>=n[0]:
    big=n[3] 
elif n[2]>=n[3] and n[2]>=n[4] and n[2]>=n[1] and n[2]>=n[0]:
    big=n[2] 
elif n[1]>=n[3] and n[1]>=n[2] and n[1]>=n[4] and n[1]>=n[0]:
    big=n[1]
else:
    big=n[0]
print("Biggest num among 5 =",big)