#Running code which can through error or not.
print("Enter no.1")
num1=(input())
print("Enter no.2")
num2=(input())
try:
    print("The Sum is :: ",
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("This is important")