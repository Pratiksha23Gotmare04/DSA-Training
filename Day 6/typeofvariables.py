#---------------------- Type of variable(instance var) ------------------------#
# instance variable depends on the state of the object
# using class name we can modify, add , change the values but by object we cann't

# class New:
#     def __init__(self):
#         self.a = 10

# obj1 = New()
# obj2 = New()
# obj3 = New()
# #obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#------------------------- Type of variable static variable ------------------------------#

# class New:
#     def __init__(self):
#         self.name = "Pratiksha"

# obj1 = New()
# obj2 = New()
# obj3 = New()
# New.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#--------------------------------------------------------------------------------------#

# for every object a separate copy of instance variable is created
# but in case of static variable only one copy will be created
# and it is accessible for every object of the class

class College:
    collegename = "RCOEM College"   # static variable (1 memory)

    def __init__(self):
        self.studentname = "Pratiksha"   # instance variable (3 separate memory)


principal = College()    # object creation
teacher = College()
accountant = College()

print("principal=", principal.collegename, ":", principal.studentname)
print("teacher =", teacher.collegename, ":", teacher.studentname)
print("accountant=", accountant.collegename, ":", accountant.studentname)

College.collegename = "RBU"   # second way to add static variable
principal.studentname = "Pratiksha Gotmare"

print("principal=", principal.collegename, ":", principal.studentname)
print("teacher =", teacher.collegename, ":", teacher.studentname)
print("accountant=", accountant.collegename, ":", accountant.studentname)
