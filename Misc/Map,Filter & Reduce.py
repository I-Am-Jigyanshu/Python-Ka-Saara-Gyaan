# ----------------------MAP-------------------------- #

# map == ek function ko puri list main apply kr deta hai
numbers = ["3","4","6"]
numbers = list(map(int, numbers))


# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2]+1
# print(numbers[2])
# def sq(a):
#     return a*a
# num = [2,3,4,5,25,36,7,8,9]
# square = list(map(sq,num))
# print(square)


# num = [2,3,4,5,25,36,7,8,9]
# square = list(map(lambda x: x*x , num))
# print(square)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [square,cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# ------------------FILTER----------------------------------- #

# filter == list bnata hai jispe function true return krta ho
# list_1 = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

# ----------------REDUCE-----------------------------------#
from functools import reduce

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
print(num)
# num = 0
# for i in list1:
#     num = num + i
# print(num)
