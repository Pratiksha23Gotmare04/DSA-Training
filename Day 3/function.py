#----------------------------- WHILE LOOP--------------------------------------#
# i = 1
# while i <= 5:
#     print(i)
#     i = i +1 

#-------------------------------------------------------------------------------------------------#

# def hello():  # called function
#     print("Hello, World")
# hello()   # calling function 

#----------------------------------------------------------------------------------------------------#
# It is possible to return multiple values = Yes 
# def arithmetic():
#     a = int(input("Enter the value of a : "))
#     b = int(input("Enter the value of b : "))
#     sum = a + b 
#     sub = a - b 
#     mul = a * b 
#     div = a / b
#     return sum, sub, mul, div 
# #print(arithmetic())   # print the values in the tuple form

# result = arithmetic()
# print(result)

#---------------------------------------------------------------------------------------------------------#
"""
# How many types of argument we pass in function ?
# 1. positional argument  2. keyword argument  3.Default argument  
# 4.variable length/variable no of argument 

# 1. Positional argument
def arithmetic(a, b):
    sum = a + b 
    sub = a - b 
    mul = a * b 
    div = a / b
    return sum, sub, mul, div
result = arithmetic(5, 5)       # positional argument
print("Arithmetic : " ,result) 


# 2.Keyword Argument (Parameter name and key name must be same)
def credential(username, password):
    if username == password:
        print("login Successfully")
    else:
        print("Invalid credential")
credential(username = "admin", password = "admin")

# 3.Default argument
def cityName(city = "Pune"):
    print(city)
cityName("Nagpur")
cityName("Mumbai")
cityName()

# 4.Variable length / Variable no of argument
def cityName(*name):           # (*) ensure that the all the parameter are accepted
    print(name)
cityName("Nagpur", "Mumbai", "Pune", "Delhi") 
"""

#----------------------------------------------------------------------------------------------------------#

# Modularity aaproach in function
import sys 
def add():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a + b)

def sub():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a - b)

def mul():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a * b)

def div():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a / b)

while True:
    print("1.Addition ")
    print("2.Subraction ")
    print("3.Multiplication ")
    print("4.Division ")
    print("5.Exit")
    choice = int(input("Enter your choice : ")) 
    if choice == 1:
        add()     # calling function
    elif choice == 2:
        sub() 
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()          # sys = predefined function










