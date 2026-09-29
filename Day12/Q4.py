"""
Q4. Write a Python program using a Product class with 
product ID, name, price, and quantity. Define methods to 
calculate and display the total bill. Use els to access the 
attributes and methods. Accept all product information from 
the user and create an object to perform the operations.
"""
r=lambda price,quantity: price*quantity
class Product:
    def Display(self, id, name, price, quantity):
        print("Product ID:",id)
        print("Name:", name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Total Bill: ₹", r(price,quantity))

p=Product()
id=int(input("Enter Product ID:"))
name=input("Enter Name:")
price=float(input("Enter Price:"))
quantity=int(input("Enter Quantity:"))
p.Display(id,name,price,quantity)