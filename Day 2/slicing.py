# name = 'PratikshaGotmare'
# print(name[0])    # P
# print(name[1])    # r
# print(name[-1])   # e
# print(name[15])   # e
# print(name[0:5])  # Prati
# print(name[1:])   # ratikshaGOtmare
# print(name[:5])   # Prati
# print(name[:])    # PratikshaGotmare
# print(name[1:8:2])  # rtkh
# print(name[::-1]) # reverse of string 

#----------------------------------------------------------------------------------------------------#
# s = "Python are high level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())   # swapping l - u and u - l
# print(s.title())      # first letter of every letter of s is capital
# print(s.capitalize()) # first letter of the s capital 

#----------------------------------------------------------------------------------------------------#
# Format Function
# name = "Pratiksha"
# sal = 5000
# age = 22
# print("{} sal is {} age is {}" .format(name, sal, age))
# print("{0} sal is {1} age is {2}" .format(name, sal, age))
# print("{x} sal is {y} age is {z}" .format(x = name, y = sal, z = age))
# A = 1
# print(f"{A} is a good boy")

#----------------------------------------------------------------------------------------------------#
# name = "Pratiksha"
# for i in name:
#     print(i)

#----------------------------------------------------------------------------------------------------#
#WAP to remove duplicate character
# name = "Pratiksha"
# result = ""
# for i in name:
#     if i not in result:
#         result += i
# print(result)

# #WAP to reverse by using loop
# res = ""
# N = len(name)
# for i in range(N-1, -1, -1):
#     res += name[i] 
# print(res)

#----------------------------------------------------------------------------------------------------#
#WAP to check if it is palindrome number or not
# name = input()
# result = name[::-1]
# print(result)
# if name == result:
#     print("Palindrome Number")
# else:
#     print("Not a palindrome Number")

#-----------------------------------------------------------------------------------------------------------------
#WAP to check if it armstrong number or not

# number = int(input("Enter a number : "))
# sum = 0
# temp = number
# while temp > 0:     
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if number == sum:
#     print("Armstrong Number")   
# else:    
#     print("Not an Armstrong Number")

#---------------------------------------------------------------------------------------------------------------------#
#WAP to count vowels and consonant
# name = input()
# vowels = 0
# consonant = 0
# for i in name:
#     if i in "aeiouAEIOU":
#         vowels += 1
#     else:
#         consonant += 1 
# print("Vowels : ", vowels)
# print("Consonant : ", consonant)

# Another Method
# vowels = ['a', 'e', 'i', 'o', 'e']
# name = "hello"
# cons = 0
# vow = 0
# for i in name:
#     if i in vowels:
#         vow += 1 
#     else:
#         con += 1 
# print(cons)
# print(vow)


#---------------------------------------------------------------------------------------------------------------------#
# WAP to check for anagram - input(listen, slient) output(Anagram)
str1 = input()
str2 = input()
if sorted(str1) == sorted(str2):
    print("Anagram String")            
else:
    print("Not an Anagram String")


#---------------------------------------------------------------------------------------------------------------------#
# WAP to count word in a string
string = input()
count = 1 
for i in string:
    if i == " ":
        count += 1
print(count)

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
