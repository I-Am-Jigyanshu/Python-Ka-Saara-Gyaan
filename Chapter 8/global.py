"""
l =10 # global - kitne bhi function

def function(n):
   # l=5 # Local Variable
    m=8 # Local variable bhar print nhi krega
    # l=l+45. will through an error. No Local
    global l # permission
    l=l=45
    print(l,m)
    print(n,"I have printed")
function("This is me.")
# print(m)
"""
x=55
def Jiggu():
    x =20
    def rohan():
        global x
        x=88
    #print("Before calling Rohan()",x)  #20
    rohan()
    print("after calling rohan()",x)   #20
Jiggu()
print(x)