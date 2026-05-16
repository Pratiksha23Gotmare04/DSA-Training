# Que 1 -----------------------------------------------------------------------------#

# def func(value, values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# func(t, v)
# print(t, v[0])

# Que 2 ------------------------------------------------------------------------------#

# def f(i, values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)    
# f(3)

# Que 3 --------------------------------------------------------------------------------#

# fruit = {}     # {'Apple': 1, 'Banana':1, 'apple':1}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))           # 3

# Que 4 -------------------------------------------------------------------------------#

# v = ['a', 'e', 'i', 'o', 'u']
# w = input("Enter the word where we will search the vowels :")
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print("Found Vowels : ", found)
# print("Unique Vowels : ", len(found), 'from the given word = ', w)

# Que 5 -------------------------------------------------------------------------------#

# import datetime
# date = datetime.datetime.now()
# print("It's now : {:%d/%m/%Y %H:%M:%S}".format(date))

# Que 6 ---------------------------------------------------------------------------------#

# x = ['A', 'B', 'C']
# y = ['A', 'B', 'C']
# z = [1, 2, 3, 4]
# print(x == y)
# print(x == z)
# print(x!= z)

# -------------------------- lIST COMPREHENSION ------------------------------------#

# val =[2 ** i for i in range(1,6)]   # 1, 2, 3, 4, 5
# print(val)

# s = [i*i for i in range(1,11)]
# print(s)

#-------------------------- DICTIONARY COMPREHENSION ----------------------------#

# sqr = {x: x*x for x in range(1,6)}
# print(sqr)

# double = {x: 2*x for x in range(1,6)}
# print(double)

#-------------------------- OPERATORS PRECEDENCE --------------------------------#

# a,b = [int(x) for x in input("Enter 2 number :").split()]
# print("Product is :", a*b)

# a,b,c = [float(x) for x in input("Enter 3 number :").split(',')]
# print("The sum is:", a+b+c)

#----------------------- USING ELSE BLOCK ------------------------------#
# mycart = [10, 20, 800, 60, 70]
# for item in mycart:
#     if item > 400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have purchased everything")

#---------------------------------------------------------------------------#

# username = input("Enter username : ")
# password = input("Enter password : ")

# if username == "admin" and password == "admin123":
#     print("Login Successfull")
# else:
#     print("Invalid Credential")
#     username = input("Enter username :")
#     password = input("Enter password : ") 

#----------------------------------------------------------------------------#



