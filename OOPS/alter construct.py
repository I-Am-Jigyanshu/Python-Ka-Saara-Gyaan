class Employee:
    no_of_leaves = 8 # sab ke liye same h
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printDetails(self): # vo object jiski baat ki jaa rhi hai
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))




jiggu = Employee("Jiggu",255,"Instructor") #argument goes to init
karan = Employee.from_dash("Karan-480-Student")
# rohan = Employee()
print(karan.no_of_leaves)

# jiggu.name = "Jiggu"
# jiggu.salary = 455
# jiggu.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4556
# rohan.role = "Student"
# print(rohan.printDetails())
# print(jiggu.printDetails())
# jiggu.change_leaves(24)
# print(jiggu.no_of_leaves)
