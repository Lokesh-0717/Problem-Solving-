class Shape:
    name="Shape name"
class Circle(Shape):
    def area(self):
        r=int(input("Enter r value : "))
        area_circle=3.14*r*r
        print("Area of Circle : ",area_circle)
class Rectangle(Shape):
    def area(self):
        l=int(input("Enter Length value : "))
        b=int(input("Enter Breadth value : "))
        area_rect=l*b
        print("Area of Rectangle :",area_rect)
class Triangle(Shape):
    def area(self):
        a=int(input("Enter Base value : "))
        h=int(input("Enter Height value : "))
        area_tri=0.5*a*h
        print("Area of Triangle : ",area_tri)
        
c=Circle()
r=Rectangle()
t=Triangle()
c.area()
r.area()
t.area()