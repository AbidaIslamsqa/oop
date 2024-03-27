jhon = ["Jhon Doe" , 30 , "Maneger" , 2001 , 30000]
bob = ["Bob merley", 27 , "Developer" , 2007 , 20000]
alice = ["Alice spock" , 25 ,"HR" , 2015 , 15000]
class employee:
    employeetype = "Fulltime"
    def __init__(self , name , age , designation , joiningyear , salary):
        self.name1 = name
        self.age1 = age
        self.designation1 = designation
        self.joiningyear1 = joiningyear
        self.salary1 = salary
    def promote(self , promoteddesignation):
        self.promote1 = promoteddesignation
    def salaryincrement(self , increment):
        self.salary1 += increment
jhon = employee("Jhon Doe" , 30 , "Maneger" , 2001 , 30000)
bob = employee("Bob merley", 27 , "Developer" , 2007 , 20000)
#print(jhon.name1 , '\n' , jhon.employeetype)
#print(jhon==bob)
print(jhon.name1 ,"is a" , jhon.designation1)
jhon.promote("Director")
print(jhon.name1 , "is promoted as" , jhon.promote1)
jhon.salaryincrement(10000)
print(jhon.name1 , "new salary is" ,jhon.salary1)
bob.salaryincrement(5000)
print(bob.name1, "new salary is" , bob.salary1)