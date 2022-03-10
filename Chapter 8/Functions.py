'''
a = 9
b=8
c=sum((a,b)) #built in function
print(c)
'''
#def function(a,b): #user defined Function
    #print("Hello World",a+b)
def function1(a,b):
    """This is a function which will calculate average of two numbers.""" #docstrings
    average = (a+b)/2
    #print(average)
    return average # now it will return value

#function1(5,7)
#v = function1(5,7) # will return none
#print(v)

print(function1.__doc__)
