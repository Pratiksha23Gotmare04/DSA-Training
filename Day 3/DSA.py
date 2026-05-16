# DS are different ways of organizing data on your computer, that can be used effectively.

# find biggest no

# def findBiggestNo(sampleArray):     # [5, 7, 9, 2, 3, 13]
#     biggestNo = sampleArray[0]      # BN = 5                  # ================> O(1)
#     for index in range(1, len(sampleArray)):   # index = 13   # ================> O(N)
#         if sampleArray[index] > biggestNo:     # 13 > 9       # ================> O(1)
#             biggestNo = sampleArray[index]     # 13           # ================> O(1)
#     print(biggestNo)                                          # ================> O(1)
# sampleArray = [5, 7, 9, 2, 3, 13]                             # ================> O(1)
# findBiggestNo(sampleArray)                                    # ================> O(1)
                                                                # ===========>Final O(N)

#----------------------------------------------------------------------------------------------------------#
# def foo(array):
#     sum = 0
#     product = 1
#     for i in array:
#         sum += i 
#     for i in array:
#         product *= i 
#     print("Sum = " + str(sum) +", Product = " + str(product))  

#-------------------- Row Wise Max Value ----------------------#
# mylist = [[100,198,333,323],
#           [122,232,221,111],
#           [223,565,245,764]] 
# newlist =[]
# for i in range(3):    # i = 0
#     j = 0
#     max =  mylist[i][j]   # max = 100
#     for j in range(4):
#         c_max = mylist[i][j]   
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)

#---------------------------------------------------------------------------------------------#
# input = 'praiksha*is*a*good*programmer'

# name = 'pratiksha*is*a*good*programmer'
# newname = ''
# val = ''
# for i in name:
#     if i != '*':
#         newname += i
#     else:
#         val += i 
# print(newname)
# print(str(val+newname))

#-------------------------------------------------------------------------------------------------------------#
# input = aaabbbbccceeeee    output = a3b4c3e5
# name = 'aaabbbbccceeeee'
# newname = ''
# count = 1
# for i in range(len(name)-1):
#     if name[i] == name[i+1]:
#         count += 1
#     else:
#         newname += name[i] + str(count)
#         count = 1
# newname += name[-1] + str(count)
# print(newname)



