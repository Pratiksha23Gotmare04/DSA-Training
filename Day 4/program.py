#---------------------------------------------------------------------#

# name = 'aaabbbbccceeeee'
# newname = {}
# for i in range(len(name)):
#     key = name[i]
#     count = 0
#     for j in range(len(name)):
#         if key == name[j]:
#             count += 1
#     newname[key] = count 

# for i, j in newname.items():
#     print(i,j,sep = '',end = '')

#------------------------------------------------------------------------#

# salary = int(input('Enter your salary:'))
# rating = int(input('Enter your performance apparisal rating : '))
# increment = 0
# if rating >= 1 and rating <= 3:
#     increment = salary * 10/100
# elif rating >= 3.1 and rating <= 4:
#     increment = salary * 30/100
# elif rating >= 4.1 and rating <= 5:
#     increment = salary *40/100
# else:
#     print('Invalid rating')
# print('Increment Salary:', increment+salary)

#--------------------------------------------------------------------------------#
"""
basic salary = 20000
so we have to calculate the
HRA of basicsalary = 20%
TA of basicsalary = 30%
DA of basicsalary = 45%
calculate GrossSalary = ?
"""

BS = int(input("Enter the BasicSalary : "))
HRA = BS * (20/100)
TA = BS * (30/100)
DA = BS * (45/100)
GS = BS-(HRA + TA + DA) 
print("GrossSalary : ", GS)