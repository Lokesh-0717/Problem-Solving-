class Vehicle:
    Brand="Hero Honda"
    Model= 2026
    def Display_details(self):
        print("One of the best Automobile Company")
class Bike(Vehicle):
    Product_name="Activa"
class Car(Vehicle):
    Variant="Casual"
    
b=Bike()
c=Car()
b.Display_details()
c.Display_details()
print(b.Product_name)
print(c.Variant)