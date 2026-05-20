# Que 1 : Remove leading zeros from a list of integer -----------------#
"""
Write a function to remove the leading zeros from a list of integers.
Logic:
Use list slicing or a loop to remove zeros until a non-zero element is encountered.
Sample Input:
[0, 0, 1, 2, 0, 3, 0, 0, 4]
Sample Output:
[1, 2, 0, 3, 0, 0, 4]
"""

def removeLeadingZero(list):
    i = 0
    while i < len(list) and list[i] == 0:
        i += 1
    return list[i:]
list = [0, 0, 1, 2, 0, 3, 0, 0, 4]
print(removeLeadingZero(list))

#-------------------------- EXCEPTION HANDLING ------------------------------#
"""We can take multiple exception at the single except block.  
except(ZeroDivisionError, ValueError):
    print(msg)

    OR
    
except(ZeroDivisionError):
    print("Error: Division by zero is not allowed.")
except(ValueError):
    print("Error: Invalid input. Please enter a valid number.") 


"""
# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
#     print(a/b)
# except(ZeroDivisionError):
#     print("Error: Division by zero is not allowed.")
# except(ValueError):
#     print("Error: Invalid input. Please enter a valid number.") 
# except:
#     print("An unexpected error occurred.")

#-----------------------------------------------------------------------#

# import logging

# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)

# try:
#     a = int(input("Enter first integer number : "))
#     b = int(input("Enter second integer number : "))

#     print(a / b)

# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)

# print("Logging Level is set up. Check 'newfile.txt' for log details.")
