# def function_name_print(a,b,c,d):
#
#     print(a,b,c,d)
def funargs(normal,*args, **kwargs):
    print(normal)

    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
     # As a tuple
# function_name_print("Jiggu","g","f","dd")
list = ["Jiggu","g","f","dd"]
normal = "Yhis is normal"
kw = {"Rohan":"Monitor", "Jiggu":"Sports coach","Him":"Programmer"}
funargs(normal,*list,**kw)