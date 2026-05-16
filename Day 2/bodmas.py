# # BODMAS
# a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)   # 160
# print((a-b)*(c/d)) # 40
# print(a+(b*c)/d)   # 110

#-----------------------------------------------------------------------------------------------------------------#

# string = input()
# count = 0
# str = ord(string)
# for i in str:
#     if (str >= 65 and str <= 97) or (str >= 97 and str <= 122) or (str >= 48 and str <= 57):
#         continue
#     else:
#         count += 1 
# print(count)

#-------------------------------------------------------------------------------------------------------------#

# str = input()
# print(str.title())

#------------------------------------------------------------------------------------------------------------------------#
# print('Pratiksha'.isalnum())
# print('Pratiksha23'.isalnum())
# print('2334f'.isdigit())
# print('sdfra'.islower())
# print(''.islower())
# print('PRATIKSHA'.isupper())
# print('My Name Is Pratiksha'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))


# print("Pratiksha".find("z"))
# print("Pratiksha".index("r"))
# print("Pratiksha".find("r"))
# print("Pratiksha".count("a"))

#--------------------------------------------------------------------------------------------#

# num = 123
# a = num % 10   # 3
# num = num // 10  # 12
# b = num % 10  # 2
# c = num // 10  # 1
# rev = a*100 + b*10 + c*1
# print(rev)

# input- 123456 


# Currency 
Amount = int(input("Enter the amount:"))
print("100 notes = ", Amount // 100)
print("50 notes = ", (Amount % 100) // 50)
print("20 notes = ", ((Amount % 100) % 50) // 20)
print("10 notes = ", (((Amount % 100) % 50) % 20) // 10)
print("5 notes = ", ((((Amount % 100) % 50) % 20) % 10) // 5)
print("2 notes = ", (((((Amount % 100) % 50) % 20) % 10) % 5) // 2)
print("1 notes = ", ((((((Amount % 100) % 50) % 20) % 10) % 5) % 2) // 1)



