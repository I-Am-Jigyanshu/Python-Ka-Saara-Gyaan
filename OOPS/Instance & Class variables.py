class Employee:
    no_of_leaves = 8 # sab ke liye same h
    pass

jiggu = Employee()
rohan = Employee()

jiggu.name = "Jiggu"
jiggu.salary = 455
jiggu.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4556
rohan.role = "Student"

print(jiggu.no_of_leaves)
print(rohan.__dict__)
Employee.no_of_leaves = 9 # will only change using class
print(Employee.no_of_leaves)


""" Instance se aap class ke variable ko change nhi kr skte 
"""