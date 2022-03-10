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



    def __add__(self,other):
        return self.salary + other.salary
    def __truediv__(self,other):
        return self.salary / other.salary
    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 = Employee("Jiggu",343,"Programmer")
# emp2 = Employee("Karan",34,"Cleaner")  # str>>>rpr
print(repr(emp1))
"""Mapping Operators to Functions.."""

