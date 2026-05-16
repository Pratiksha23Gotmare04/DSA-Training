""" Que 1
The garments company Apparel wishes to open outlets at various locations. 
The company shortlisted several plots in these locations and wishes to select 
only plots that are square-shaped. Write an algorithm to help Apparel find the 
number of plots that it can select for its outlets.
Input:- 
The first line of the input consists of an integer numOfPlots, representing the number 
of plots shortlisted by the company for outlets (N).
The second line consists of N space-separated integers - area1, area2, .... , areaN 
representing the area of the N plots selected for outlets.
Output:-
Print an integer representing the number of plots that will be selected for outlets.
Input:- 8
         #79 77 54 81 48 34 25 16 
Output:- 3

"""

# N = int(input())
# n = map(int, input().split())
# count = 0
# for num in n:
#     for i in range(1,num+1):
#         if i*i == num:
#             count += 1
#             break   
# print(count)

#-----------------------------------------------------------------------------#

""" Que 2
WAP to accept student name and marks from the keyboard and creates a dictionary. 
Also display student marks by taking student name 
"""

# n = int(input("Enter the number of students : "))
# d = {}
# for i in range(n):
#     name = input("Enter student name : ")
#     marks = int(input("Enter student marks : "))
#     d[name] = marks           # add key:value
# print(d)
# while True:
#     name = input("Enter student name to get marks : ")
#     marks = d.get(name, -1)
#     if marks == -1:
#         print("Student Not Found")
#     else:
#         print("The marks of ", name, "are", marks)
    
#     option = input("Do you want to find another student marks [Yes/No] : ")
#     if option == "No":
#         break 
# print("Thank for using our application")

#-----------------------------------------------------------------------------#

"""" Que 3
WAP to access each character of string in forward and backward direction using by 
using while loop?
I/P = "Learning Python is very easy"
"""

# s = "Learning Python is every easy"
# i = 0
# n = len(s)
# print("String In Forward Direction")
# while i < n:
#     print(s[i] , end = ' ')
#     i += 1 
# print()
# print("String In Backward Direction")
# i = -1
# while i >= -n:
#     print(s[i], end = ' ')
#     i -= 1

#-----------------------------------------------------------------------------#

""" Que 2
A company provides network encryption for secure data transfer. The data string is 
encrypted prior to transmission and gets decrypted at the receiving end. But due to 
some technical error, the encrypted data is lost and the received string is different 
from the original string by 1 character. Arnold, a network administrator, is tasked with 
finding the character that got lost in the network so that the bug does not harm other 
data that is being transferred through the network.

Write an algorithm to help Arnold find the character that was missing at the receiving 
end but present at the sending end.

Input
The input consists of two space-separated strings — stringSent and stringRec, 
representing the string that was sent through the network and the string that was 
received at the receiving end of the network, respectively.

Input = abcdfjgerj abcdfjger
Output = Character j at the end of the string was lost in the network during transmission.

"""
# str1 = 'abcdfjgerj'
# str2 = 'abcdfjger'

# for i , j in zip(str1, str2):
#     if i != j:
#         print(i)
#         break
# if len(str1) > len(str2):
#     print(str1[-1])

#-----------------------------------------------------------------------------#

"""Que 4
A company wishes to provide cab service for their N employees. The employees have 
distance ranging from 0 to N-1. The company has calculated the total distance from 
an employee's residence to the company, considering the path to be followed by the 
cab is a straight path. The distance of the company from itself is 0. The distance 
for the employees who live to the left side of the company is represented with a 
negative sign. The distance for the employees who live to the right side of the company 
is represented with a positive sign. The cab will be allotted a range of distance. 
The company wishes to find the distance for the employees who live within the particular 
distance range.

Write an algorithm to find the distance for the employees who live within the 
distance range.

Input

The first line of the input consists of three space-separated integers - num, start and 
end representing the size of the list (N), the starting value of the range, and the 
ending value of the range, respectively.

The second line of the input consists of N space-separated integers representing the 
distances of the employees from the company.

Output

Print the distances that lie within the given range.

Example

Input:
6 30 50
29 38 12 48 39 55
Output:
38 48 39

"""

# num, start, end = map(int, input().split())
# N = list(map(int, input().split()))
# newlist = []
# for i in range(num):
#     if start <= N[i] <= end:
#         newlist.append(N[i])
# print(*newlist)

#-----------------------------------------------------------------------------#