class Shape:
    def area(self):
        pass
class circle(Shape):
    def area(self,r):
        print("Area of circle:",3.14*r*r)
class triangle(Shape):
    def area(self,a,b):
        print("Area of triangle:",0.5*a*b)
class Rectangle(Shape):
    def area(self,a,b):
        print("Area of Reactangle:",a*b)
c,t,r= circle(),triangle(),Rectangle()
c.area(5)
t.area(5,2)
r.area(5,4)