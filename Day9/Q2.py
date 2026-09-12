#Print highest temparature city
city={}
n=int(input("Enter no.of cities="))
for i in range(n):
    key=input("city name=")
    value=float(input("Temperature="))
    city[key]=value
high=max(city.values())
for t in city:
    if city[t]==high:
        print("City with highest temperature is:",t,"with temperature",high)