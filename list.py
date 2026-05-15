mylist = ["Pratiksha", "Komal", "Abhishek", 77, "Priya", 90.09, "Prachi", "Shweta"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

# mylist[2] = "Akshay"
# print(mylist)

# if "Ankush" in mylist:
#     print("Yes Ankush is available")
# else:
#     print("Not available")

# mylist.append('Suhani')  # it stores at the top of the list
# mylist.append('Vaishnavi')
# print(mylist)
# append() and extend() both work like same

# mylist.insert(3, "Pooja")
# print(mylist)

# mylist.remove("Prachi")
# print(mylist)

# newlist = mylist.copy()   #cloning
# print(newlist)

#----------------------------------------------------------------------------------------------#
# mylist = [['Pratiksha', 'Gotmare'], ['23.5'], [44532, "yyy"]]
# print("Example Multi- dimensional list: ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list2 = [50, 23, 54, 'Pratiksha']
# del list2
# print(list2)

list2 = [50, 23, 54, 'Pratiksha']
del list2[2]
print(list2)

list2 = [50, 23, 54, 'Pratiksha']
list2.clear()
print(list2)

# name = "Pratiksha"
# print(name)
# myname = list(name)  # typecasting
# print(myname)       # print as each character seprately

#---------------------------------------------------------------------------------------------------------#
#sorting example
# mylist = [22, 34, 45, 56, 67, 12]
# mylist.sort()
# mylist.sort(reverse = True) # for desc order
# print(mylist)

""" default sorting order for number is ascending order
    default sorting order for string is alphabetical order
    we should know that list should contain homogeneous data on python2 
    first short number then string follow """

#----------------------------------------------------------------------------------------------------#
#alising means assignment one variable reference to another
#variable
# mylist = [23,31,11, 34,56, 32]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

#--------------------------------------------------------------------------------------------------------------------#
# mylist = [21,31,88, 53, 10, 45, 21]
# for i in mylist:
#     print(i)

# list = [0, 1, 4, 0, 2, 5]
# for i in list:
#     if i == 0:
#         list.remove(i)
#         list.append(i)
# print(list)

#--------------------------------------------------------------------------------------------------#
#Que 1
# list1 = [7, 3, 9, 2, 8]
# list1.sort()
# print(list1[-2])

# #Que 2
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[::2] = 10, 20, 30, 40, 50, 60 # attempt to assign sequence of size 6 to extended slice of size 5
# print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[::2] = 10, 20, 30, 40, 50 # provides solution
# print(a)

#Que 3
# a = [1, 2, 3, 4, 5]
# print(a[3:0:-1]) # print by indexing in reverse order

#Que 4
# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4): # it only focused on the rows - each row last element is pop
#     print(arr[i].pop())

#Que 5
# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i-1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ")

#Que 6
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20 
# print(sum)

#Que 7 
# A = [1, 2, 3]
# B = [2, 3, 4]
# C = [3, 4, 5]
# for i in A:
#     if i in B and i in C:
#         print(i)

#Que 8
N = int(input())
mylist = []
for i in range(N):
    val = int(input())
    mylist.append(val)
sum = 0
for i in range(len(mylist) - 1):
    if i+1 in range(len(mylist)):
        sum += abs(mylist[i] - mylist[i+1]) 
print(sum) 

