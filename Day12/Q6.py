"""
Q6. Write a Python program to demonstrate polymorphism using
      Circle, Rectangle, Triangle and Square classes.
1.	Define area() in all classes. 
2.	Accept dimensions and create objects. 
3.	Calculate and display each area. 
4.	Use a common collection and loop. 
5.	Demonstrate polymorphism using area().

"""
class Circle:
    def area(self,r):
        return 3.14*r*r
class Rectangle:
    def area(self,l,b):
        return l*b
class Triangle:
    def area(self,b,h):
        return 0.5*b*h
class Square:
    def area(self,s):
        return s*s
c,r,t,s=Circle(),Rectangle(),Triangle(),Square()
print("Area of Circle:",c.area(5))
print("Area of Rectangle:",r.area(5,4))
print("Area of Triangle:",t.area(5,4))
print("Area of Square:",s.area(5))