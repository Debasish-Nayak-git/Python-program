"""
Q5. Write a Python program using an ElectricityBill class 
with consumer number, name and units as attributes. Calculate 
the bill using:
	Up to 100 units → ₹2/unit
	101–200 units → ₹3/unit
	Above 200 units → ₹5/unit
Use methods, @staticmethodand user input to calculate and 
display the bill.
"""
r=lambda units: (units * 2 if units <= 100 else 
            (100 * 2) + ((units - 100) * 3) if units <= 200 else 
                 (100 * 2) + (100 * 3) + ((units - 200) * 5))
class Bill:
    @staticmethod
    def calculate_bill(cons_num, name, units):
        print("Consumer Number:", cons_num)
        print("Name:", name)
        print("Units:", units)
        print("Bill: ₹", r(units))

num= int(input("Enter Consumer Number: "))
name = input("Enter Name: ")
units = int(input("Enter Units: "))
Bill.calculate_bill(num, name, units)
