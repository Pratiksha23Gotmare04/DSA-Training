#Why python is called dynamically typed language?
# age = 22
# pi = 3.14
# name = "Pratiksha"
# result = True
# print(type(age))
# print(id(age)) # use to return the address of the variable in memory

# print(type(pi))
# print(id(pi))

# print(type(name))
# print(id(name))

# print(type(result))
# print(id(result))


#Why all fundamental data types are immutable in Python?
# math = 50
# chem = 50
# phy = 50
# print(id(math))
# print(id(chem)) 
# print(id(phy))

#Time Complexity = O(1)
#Simple if

# a = int(input("Enter any single digit number:"))
# if a> 0:
#     print("Positive number")
# if a < 0:
#     print("Negative number")
# if a == 0:
#     print("Zero")

# day = input("Enter a day of the week: ")
# if day == "SATURDAY" or day == "saturday" or day == "SUNDAY" or day == "sunday":
#     print("Weekend")
# else:
#     print("Working")

# percentage = 65
# if percentage >= 65:
#     print("Grade A")
# elif percentage <= 65 and percentage >= 50:
#     print("grade B")
# else:
#     print("Fail")

#----------------------------------------------------------------------------------------------#
#ASCII = Use in C and CPP
#Unicode = Ude in Java and Python
#ORD function used to convert into unicode

# chr = ord(input("Enter any one character : "))
# if chr >= 65 and chr <= 90:
#     print("Upper Case")
# elif chr >= 97 and chr <= 122:
#     print("Lower Case")
# elif chr >= 48 and chr <= 57:
#     print("Digit")
# else:
#     print("Special character")

#--------------------------------------------------------------------------------------------#
# Membership Operator(IN and NOT IN)
# name = "help4code"
# print('z' in name)
# print('z' not in name)
# print('p' not in name)

#----------------------------------------------------------------------------------------------#
# Identity Operator(IS and IS NOT) = purpose(for address comparison)
# math = 50
# chem = 50
# print(math is chem)
# print(math is not chem)

#-------------------------------------------------------------------------------------------------------------#
#for(initialization; condition; inc/dec)
# for i in range(5): # automatically increment
#     print(i)

# for i in range(2,10,2): # incremented by 2
#     print(i)

# for i in range(5, 0, -1): #dec by 1 
#     print(i)

# for i in range(1,11):
#     print(2*i)

# for i in range(1, 11):
#     print(1*i, " ", 2*i, " " , 3*i, " ", 4*i, " ", 5*i, " " , 6*i, " " , 7*i, " ", 8*i, " ", 9*i, " ", 10*i)
# print()
# for j in range(1,11):
#     print(11*i, " ", 12*i, " " , 13*i, " ", 14*i, " ", 15*i, " " , 16*i, " " , 17*i, " ", 18*i, " ", 19*i, " ", 20*i)

# #------------------------------------------------------------------------------------------------------------------------------#
""" WAP to accept three paper marks and calculate total, per, 
and check if he/she is passed in all the subject 
so print pass else print fail
if per is greater than 65 and greater = "male" so he is eligible for placement else not eligible
"""

# sub1 = int(input("Enter the marks of sub1: "))
# sub2 = int(input("Enter the marks of sub2: "))
# sub3 = int(input("Enter the marks of sub3: "))
# total = sub1 + sub2 + sub3
# print("Total :", total)
# per = total/3.0
# print("Percentage :", per)

# if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
#     print("Pass")
# else:
#     print("Fail")

# gender = input("Enter your gender M/F : ")
# if per >= 65 and gender == "M":
#     print("Eligible for Placement")
# else:
#     print("Not Eligible")

#----------------------------------------------------------------------------------------------------------------------------------------------------#
# for i in range(1,5):
#     if i == 3:
#         break 
#     print(i)

# for i in range(1,5):
#     if i == 3:
#         continue 
#     print(i)

#zip() fuction = we an take multiple range fuction inside zip()
# for i,j in zip(range(1,6), range(5,0,-1)):
#         if i == 3 and j == 3:
#             continue 
#         print(i, " ", j)
        