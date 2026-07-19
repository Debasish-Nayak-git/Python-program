day=int(input("Enter no. of overdue date"))
second=day-5
remain=day-10
if day>10:
    fine=5*2+5*5+remain*10
elif day>5:
    fine=5*2+second*5
else:
    fine=day*2
penalty=100
if fine>500:
    fine=fine+penalty

print("total due=",fine)