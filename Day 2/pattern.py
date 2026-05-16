# Nested loop
# for i in range(1,4):
#     for j in range(1,4):
#         print(i, end = " ")
#     print()

#------------------------------------------------------------------------------------------------------------------------#

# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i), end = " ")
#     print()

#-------------------------------------------------------------------------------------------------------------------#

# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*", end = " ")
#     print()

#----------------------------------------------------------------------------------------------------------------------------#

# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j), end = " ")
#     print()

#------------------------------------------------------------------------------------------------------------------#

# import time
# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     print(" "*(n-i), end = " ")
#     for j in range(1,i+1):
#         time.sleep(3)
#         print("*", end = " ")
#     print()

#----------------------------------------------------------------------------------------------------------------------#
# input[1,2,3,4] output[24,12,8,6]
n= int(input("Enter the number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i), end = " ")
    print()