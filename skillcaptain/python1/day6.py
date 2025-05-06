# 10*(1/0) ZeroDivisionError: division by zero
# 4 + spam*3 NameError: name 'spam' is not defined
# '2' +2   TypeError: can only concatenate str (not "int") to str
# while True  print("Hello world") SyntaxError: invalid syntax

# while True :
#     try :
#         x = int (input("Please enter a number"))
#         break
#     except ValueError:
#         print("oops , that is not a number")
# Design a Python program to execute division on two predefined numbers, while considering the possibility of a division by zero error. 
# Ensure that the program handles this exception gracefully, providing a clear error message in such cases.

def division (num1 , num2) :
    try:
        print(num1/num2)
    except ZeroDivisionError :
        print(" Division by zero is not allowed.")
        

division(1,0)