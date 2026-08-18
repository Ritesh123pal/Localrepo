# create student class that takes name and marks of 3 subjectsas agrument in constructor. then create a method to print the average
class student:
   def __init__(self,fullname,physics,chem,maths):#constructor
       self.name=fullname
       self.phy_marks=physics
       self.chem_marks=chem
       self.math_marks=maths
   def hi(self):
       print("name:",self.name)

   def average(self):
       avg=(self.phy_marks + self.chem_marks + self.math_marks) / 3
       print("average_marks=",avg)
s1=student("karan",98,90,95)

s1.hi()  
s1.average()
