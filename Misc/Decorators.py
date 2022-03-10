# def function1():
#     print("Bete mauj Kardi")
#
# func2 = function1
# del function1
# func2()


# def funcret(num):
#     if num == 0:
#         return print
#     if num ==1 :
#         return int
# a = funcret(1)
# print(a)

# def executer(func):
#     func("this")
# executer(print)

def dec1(func1):
    def nowexec():
        print("Execute now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_Jiggu():
    print("Jjj")
# who_is_Jiggu = dec1(who_is_Jiggu)
who_is_Jiggu()
