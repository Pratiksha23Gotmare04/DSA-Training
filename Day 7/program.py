""" Que 1: Find the first non- repeating character
Write a function to find the first non- repeating character in a string 
Logic = Define a function that uses loops to count characters and find the first 
non repeating character.
Sample = "Leetcode"
Output = "L"

"""

def first_non_repeating(s):
    for ch in s:
        count = 0
        for c in s:
            if ch == c:
                count += 1
        if count == 1:
            return ch
    return "No non-repeating character in the string"
s = "Leetcode"
print(first_non_repeating(s))



""" Que 2: Array Rotation
Question: Rotate an array to the right by a given number of steps.
Logic:Use array slicing or create a new array to rearrange elements according to the 
rotation steps.
Sample Input:
[1, 2, 3, 4, 5] rotated by 2 steps
Expected Output:
[4, 5, 1, 2, 3]

"""

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    rotated = arr[-k:] + arr[:-k]
    return rotated
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))