"""Write a Python program using the format() method to accept N 
product details such as product ID, product name, price, and 
quantity. Calculate the total price and store the product 
records in a text file(“product.txt”). Finally, read and display
 the product details in a properly formatted manner.
"""
f=open("product.txt","w")
n=int(input("Enter the number of products: "))
for i in range(n):
    name=input("Product name: ")
    id=int(input("product id: "))
    price=int(input(" price: "))
    quantity=int(input("quantity: "))
    f.write("product Name:{0} id:{1} price:{2} quantity:{3}\n".format(name,id,price,quantity))
print("Sucessfully updated")
f.close()