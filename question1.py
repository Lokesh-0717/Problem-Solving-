class Student:
    name=input("Name : ")
    roll=int(input("Roll No : "))
    marks=int(input("Marks : "))
    def get(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
s=Student()
print(s.get())