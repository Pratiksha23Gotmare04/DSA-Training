#--------------- BINARY SEARCH ---------------------#
""" How we decide When binary or linear search is used
When large amount of data = binary search 

1.faster that linear search
2.half of the remaining elements can be eliminated at a time, instead of 
eliminating them one by one
3.BS only works for sorted array 
4. Not compulsory to visit all the index

complexity = 

"""
#---------------------------Searching Element 72 ---------------------------------------#
# def binarySearch(arrray, target):
#     low = 0
#     high = len(array)-1
#     while low <= high:
#         mid = (low+high)//2
#         if array[mid] == target:
#             return mid 
#         elif array[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,50,55,57,57,60,62,68,69,70,71,72,79,82,84,85,89]
# target = 72
# result = binarySearch(array, target)
# if result == 1:
#     print("Element Not Found")
# else:
#     print("Element Found At ", result)

#-------------------------- BUBBLE SORT ---------------------------------#

# def bubbleSort(array):
#     for i in range(len(array) - 1):  # i = 0
#         for j in range(len(array)- i - 1):   # j = 0, 1, 2, 3, 4 (if we remove -i then it iterate whole)
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#             #print(array)
#         #print()

# array = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(array)  

#------------------------------ --------------------------------------------#
"""
A company is transmitting data to another server. The data is in the form of numbers. 
To secure the data during transmission, they plan to obtain a security key that will 
be sent along with the data. The security key is identified as the count of the repeating 
digits in the data.
Write an algorithm to find the security key for the data.

Input
The input consists of an integer data, representing the data to be transmitted.
578378923

Output
Print an integer representing the security key for the given data.
3 
If no data is repeated it should display
-1

Explanation
The repeated digits in the data are 7,8 and 3.So, the security key is 3.
"""

# list = [5,7,8,3,7,8,9,2,3]
# newlist = []
# for i in range(len(list)):
#     count = 0
#     key = list[i]
#     j = i+1
#     while j < len(list):
#         if key == list[j]:
#             newlist.append(key)
#         j += 1
# print(len(newlist))


# Another Method
mylist = [5,7,8,3,7,8,9,2,3]
newdict = {}
for i in range(len(mylist)):
    count = 0
    key = mylist[i]
    j = 1
    while j < len(mylist):
        if key == mylist[j]:
            count += 1
        j += 1
    if count > 1:
        newdict[key] = count
max = newdict
print(max)

