# represented by () it is optional
# immutable

# mytuple = ("Pratiksha", "Suhani", "Vaishnavi", "Nandini", "Sudhanshu", "Tejas", 23, 23.45)
# print(mytuple)
# print(type(mytuple))

# mytuple[2] = "Rahul"  # shows error
# print(mytuple)

# Que 1
# init_tuple = ()
# print(init_tuple.__len__()) # 0 

# Que 2
# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a','b')
# print(init_tuple_a == init_tuple_b) # True

# Que 3
# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b)  # ('1', '2', '3', '4')

# Que 4
# l = [1, 2, 3]
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])    
# print(init_tuple)   # ()

# Que 5
# init_tuple = ('Python',)*3
# print(type(init_tuple))  # <class 'tuple'>

# Que 6
# init_tuple = ('Python')*3
# print(type(init_tuple))  # <class 'str'>

# Que 7
# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple) 

# Que 8 
init_tuple = ((1, 2,) * 7)
print(len(init_tuple[3:8]))  # 5

init_tuple = ((1, 2), * 7)
print(len(init_tuple[3:8]))  # 4