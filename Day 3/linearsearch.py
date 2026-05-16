#-------- LINEAR SEARCH ---------#

# def linearSearch(array, target):
#     for i in range(0, len(array)-1):     # i = 0
#         if array[i] == target:           # 1 == 7 
#             return i
#     return -1                        # if target not in the array

# array = [1, 2, 3, 4, 8, 7, 9]
# target = 7
# result = linearSearch(array, target)
# if result == -1:
#     print("Target value not found")
# else:
#     print("Element found at index ", result)

#------------- REMOVING SPACES FROM STRING ----------------------#
"""
1. rstrip() - removes spaces from the right end of the string
2. lstrip() - removes spaces from the left end of the string    
3. strip() - removes spaces from both ends of the string
"""

city = input("Enter the city name : ")
scity = city.strip()
if scity == 'Hyderabad':
    print("Hello to Hyderabad..Pratiksha")
elif scity == 'Chennai':
    print("Hello to Madrasi....Pratiksha")
elif scity == 'Bangalore':
    print("Hello to kannadiga......Pratiksha")
else:
    print("You entered the city invalid")
