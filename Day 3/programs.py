# Que 1 = Find the maximum number of consecutive 1s in a binary array.
arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]     # output = 4
count = 0
max_count = 0
for num in arr: 
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0 
print(max_count)


#--------------------------------------------------------------------------------------------------------------------#

# Que 2 = WAP to count the no of occurrences of a substring in a string
string = "abababab"    # output = 4
substring = "ab"
count = 0
for i in range(len(string) - len(substring) + 1):   
    if string[i:i+len(substring)] == substring:   
        count += 1  
print(count)    