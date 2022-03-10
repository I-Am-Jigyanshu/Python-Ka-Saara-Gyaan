class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This Employee is {self.fname}  {self.lname}"

    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return "Email is not Set.. Set it using Setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None



jiggu = Employee("Jiggu","G")
Karan = Employee("Karan","G")
jiggu.email = "HTis.tshir@gmail.com"
print(jiggu.fname)
del jiggu.email
print(jiggu.email)
