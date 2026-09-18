class Employee:
    empid=1093
    name="Ram"
    salary=20000
    def hra(self):
        hra = self.salary*0.20
        print("HRA : ",hra)
        da = self.salary*0.10
        print("DA : ",da)
        total=self.salary+hra+da
        print("Total Salary is",total)
        
emp=Employee()
emp.hra()