#Print highest temparature city
a={}
n=int(input("Enter no.of cities="))
for i in range(n):
    key=input("city name=")
    value=input("Temperature=")
    a[key]=value
high=max(a.values())
for t in a:
    if a[t]==high:
        print("City with highest temperature is:",t,"with temperature",high)