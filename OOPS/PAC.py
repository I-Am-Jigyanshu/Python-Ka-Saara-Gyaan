"""
Public -
Protected -
Private -
"""

class Employee:
    var = 8
    no_of_leaves = 8 # sab ke liye same h
    _protect = 9
    __private = 99
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
# karan = Employee.from_dash("Karan-480-Student")
rohan = Employee("Rohan",455,"Student")


class Player:
    var = 9
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printDetails(self): # vo object jiski baat ki jaa rhi hai
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgrammer(Employee, Player): # Order is imp..
    var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)

emp = Employee("Jiggu", 7,"Programmer")
print(emp._protect)
print(emp._Employee__private) # Name Mangling



 