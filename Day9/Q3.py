#product and price using dictionary 
product={}
n=int(input("Enter no. of product="))
for i in range(n):
    key=input("Enter product name=")
    value=float(input("Enter price="))
    product[key]=value
choice=input("Enter your product name=")
if choice in product:
    print("Price of",choice,"is",product[choice])