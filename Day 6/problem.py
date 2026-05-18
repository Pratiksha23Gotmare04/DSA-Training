""" Que 1
WAP to reverse each world in a string.
Logic = Split the string into words, reverse each word and join them back together
Sample Input = "Hello World
Expected Output = "olleH dlroW

By using While loop 
string = input()
n = len(string)
i = -1
while i >= -n:
    print(string[i], end = '')
    i -= 1

"""

string = "Hello World"
words = string.split()
newstring = []
for word in words:
    newstring.append(word[::-1])

result = " ".join(newstring)
print(result)

""" Que 2 : Check for valid parentheses
Write a program to check if a string containing parentheses is valid.
Logic = Use a stack to keep track of open and close parentheses.
Sample Input = "({[()]})"
Expected Output = Valid

"""

def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

""" Que 3 : 30. Find All Duplicates in a List
Write a function to find all the elements that appear more than once in a list.
Logic: Use a loop and a dictionary to count occurrences.
Sample Input: [4, 3, 2, 7, 8, 2, 1, 5, 5]
Expected Output: [2, 5]

"""

def findDuplicates(nums):
    count = {}
    duplicates = []
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    return duplicates


""" Que 4 : Sort Dictionary by key and value
Write a function to sort a dictionary by keys or values in ascending or descending order.
Logic: Use the sorted() function with a custom key or use list comprehension.
Sample Input:{"C": 3, "B": 2, "A": 1}
Expected Output (Ascending by Key):{"A": 1, "B": 2, "C": 3}
Expected Output (Descending by Value):{"C": 3, "B": 2, "A": 1}

"""

dict = {"C": 3, "A": 1, "B": 2}
# Sort by key in ascending order
sorted_by_key = dict(sorted(dict.items()))  
print("Sorted by key (ascending):", sorted_by_key)

# Sort by value in descending order
sorted_by_value_desc = dict(sorted(dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by value (descending):", sorted_by_value_desc)

