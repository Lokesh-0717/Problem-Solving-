class Stdresults:
    name="Sai"
    roll=1101
    sub1_marks=37
    sub2_marks=28
    sub3_marks=32
    def total(self):
        total = self.sub1_marks + self.sub2_marks + self.sub3_marks
        print("Total Marks : ",total)
    def average(self):
        average = self.total / 3
        print("Average is ",average)
    def grade(self):
        if(self.average>= 90):
            print("A Grade")
        elif(75>=self.average<=89):
            print("B Grade")
        elif(60>=self.total<=74):
            print("C Grade")
        elif(40>=self.total<=59):
            print("D Grade")
        else:
            print("Fail")
        
r=Stdresults()
r.total()
r.average()
r.grade()
    