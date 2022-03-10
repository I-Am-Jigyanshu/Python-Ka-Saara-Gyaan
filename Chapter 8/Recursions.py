""" Functions ke andar Functions ko use krna is Recursion.
"""
# def print2(str1):
#     print2(str1) Maximum Recursion error.
#     print("This is " + str1)
# print2("Jiggu")
# def Factorial_Iterative(n):
#     """
#
#     :param n: Integer
#     :return: n*n-1*n-2*n-3....1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
# number = int(input("Enter the Number:  "))
# print("Factorial using Iterative Method is", Factorial_Iterative(number))
# #  n! = n*n-1*n-2*n-3....1
# # n! = n * (n-1)!

def Factorial_Recursive(n):
    """

    :param n: Integer
    :return: n*n-1*n-2*n-3....1
    """
    if n == 1:
        return 1
    else:
        return n * Factorial_Recursive(n-1)

number = int(input("Enter the Number:  "))
print("Factorial using Recursive Method is", Factorial_Recursive(number))
"""
LOGIC
5 * Factorial_Recursive(4)
5 * 4 * Factorial_Recursive(3)
5 * 4 * 3 * Factorial_Recursive(2)
5 * 4 * 3 * 2 * Factorial_Recursive(1)
5 * 4 * 3 * 2 * 1 = 120....

"""