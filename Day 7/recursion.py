#--------------------------- RECURSION --------------------------------#
"""
Que : When you are going to choice recursion ?
1.When the main problem is going to be divided into similar sub problem then we 
will use recursion.
2. In preorder, postorder and inorder traversal of tree we will use recursion.
3. Recursion uses stack memory (and usus push and pop operation that is time consuming)

Que : Comparision between recursion and iteration in tewrm of time and space complexity?

                        TC               SC
Space efficiency        No               Yes      Iteration does not require extra stack 
                                                  memory, while recursion uses stack 
                                                  memory for every function call.

Time efficiency         No               Yes      Recursion takes more time because of 
                                                  repeated function calls and stack 
                                                  operations like push and pop.

Easy to use             Yes              No       Recursion is easier to write when a 
                                                  problem can be divided into smaller 
                                                  similar sub-problems.

"""

# Que 1 -----------------------------------------------------------------------------#

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
print(factorial(5))

# Que 2 -----------------------------------------------------------------------------#

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result 
    result.append(arr[0][0].upper() + arr[0][1:])     # 'car' ==> 'C+ar' ==> Car
    return result + capitalizeFirst(arr[1:])
print(capitalizeFirst(['car', 'taco', 'banana']))     # ['Car', 'Taco', 'Banana']

# Que 3 -----------------------------------------------------------------------------#

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
print(power(2,0))      # 1
print(power(2,2))      # 4
print(power(2,4))      # 16

# Que 4 -----------------------------------------------------------------------------#

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
print(productOfArray([1, 2, 3]))              # 6
print(productOfArray([1, 2, 3, 10]))          # 60

# Que 5 ------------------------------------------------------------------------------#

def reverse(string):  # pytho # pyth 
    if len(string) <= 1:
        return string
    return string[len(string)-1] + reverse(string[0:len(string)-1])
          # n # no                     
print(reverse('python'))
print(reverse('programming'))

# Que 6 -----------------------------------------------------------------------------#

def recursiveRange(num):  # 5 
    if num <= 0:          # 6 <= 0  # 5 <= 0
        return 0
    return num + recursiveRange(num-1)
      # 6 + 5 + 4 + 3 + 2 + 1
print(recursiveRange(6))

# Que 7 -----------------------------------------------------------------------------#

def isPallindrome(string):
    if len(string) == 0:
        return True 
    if string[0] != string[len(string)-1]:
        return False 
    return isPallindrome(string[1:-1])
print(isPallindrome('awesome'))         # False
print(isPallindrome('racecar'))         # True
print(isPallindrome('arfda'))           # False

# Que 8 -----------------------------------------------------------------------------#

def someRecursion(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursion(arr[1:], cb)
    return True

def isOdd(num):
    if num%2 == 0:
        return False 
    else:
        return True 
    
print(someRecursion([1, 2, 3, 4], isOdd))  # True
print(someRecursion([4, 6, 7, 8], isOdd))  # True
print(someRecursion([4, 6, 8], isOdd))     # False 

#------------------------------------------------------------------------------------#

