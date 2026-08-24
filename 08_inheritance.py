# Define a employee class with attributes :role, department, salary. This class also has a showdetail( ) method. Createan engineer class that inheritsproperties from employee and have the attribute :name and age.
class employee:
    def __init__(self,role,depart,salary):
        self.role=role
        self.department=depart
        self.sal=salary
    def showdetails(self):
         print("your role is:",self.role)
         print("your depart is:",self.department)
         print("your salary is:",self.sal)      
class engineer(employee):
    def __init__(self,name,age,role,depart,salary):
        self.name=name
        self.age=age
        super().__init__(role,depart,salary)
e1=engineer("ritesh",18,"accountant","finance","40000")
print(e1.name)
print(e1.age)
print(e1.showdetails())
