num=int(input("enter no. of consumer"))
bill=0
for i in range(num):
    unit=int(input("enter no. of unit used in month"))
    if unit<=100:
        bill=unit*2
    elif unit<=200:
        bill=100*2+(unit-100)*3
    elif unit<=400:
        bill=100*2+100*3+(unit-200)*5
    else:
        bill=100*2+100*3+200*5+(unit-400)*7
    gst=0.1*bill
    amt=bill+gst
    print("total bill=",amt)
