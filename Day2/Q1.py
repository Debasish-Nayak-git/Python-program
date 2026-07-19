a=int(input("enter a number"))
b=int(input("enter a number"))
add=a+b
sub=a-b
mul=a*b
exp=a**b
if b!=0:
    mod=a%b
    div=a/b
    floor=a//b
else:
    print("division not possible")
print("Result:")
print("add=",add)
print("substration=",sub)
print("mul=",mul)
print("div=",div)
print("mod=",mod)
print("expo=",exp)
print("floor_div=",floor)