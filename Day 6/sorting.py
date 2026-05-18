#-------------------------- INSERTION SORT --------------------------#

"""Techinical Application =
Student record sorting	           Small datasets
Banking systems	                   Nearly sorted transactions
Gaming leaderboards	               Continuous insertion
Library management	               Maintaining ordered lists
Hybrid sorting algorithms	       Small partition sorting

"""

arr = [5, 3, 8, 6, 2]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = key
print("Insertion Sort : ", arr)

#---------------------------- SELECTION SORT ------------------------------------#

"""
Method 1 = arr[i], arr[min] = arr[min], arr[i]
Method 2 = temp = arr[i]
           arr[i] = arr[min]
           arr[min] = temp
"""

arr = [20, 12, 10, 15, 2]
for i in range(len(arr)):
    min = i
    j = j+1
    while j < len(arr):
        if arr[j] < arr[min]:
            min = j 
        j = j+1 
    arr[i], arr[min] = arr[min], arr[i]
print("Selection Sort : ", arr)