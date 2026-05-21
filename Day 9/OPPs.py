#-------------------------- STATIC METHOD -------------------------#
"""
In static method we donn't take self argument

"""

# class  Student:
#     @staticmethod
#     def get_personal_detail(firstname, lastname):
#         print("Your personal detail = ", firstname, lastname)

#     @staticmethod
#     def contact_detail(mobile_no, roll_no):
#         print("Your contact detail = ", mobile_no, roll_no)

# Student.get_personal_detail("Pratiksha", "Gotmare")
# Student.contact_detail(7020691480,44)

#------------------------ SINGLE LEVEL INHERITANCE ---------------------------------#

# class College:      # parent class
#     def college_name(self):      # member function of college
#         print("Ramdeobaba University")

# class Student(College):      # child class
#     def student_info(self):      # member function
#         print("Name: Ptayiksha Gotmare")
#         print("Branch: Computer Science")

# obj = Student()      # object create child class
# obj.college_name()
# obj.student_info()

#------------------------- MULTILEVEL INHERITANCE ----------------------------------#

# class College:      # parent class
#     def college_name(self):      # member function of college
#         print("Ramdeobaba University")

# class Student(College):      # child class
#     def student_info(self):      # member function
#         print("Name: Ptayiksha Gotmare")
#         print("Branch: Computer Science")

# class Exam(Student):
#     def subject(self):
#         print("Subject1 : DBMS")
#         print("Subject2 : AI")
#         print("Subject3 : PR")

# obj = Exam()      # object create child class
# obj.college_name()
# obj.student_info()
# obj.subject()

#------------------------- MULTIPLE INHERITANCE --------------------------#

# class SubMarks:      # class-1
#     math = int(input("Enter paper marks of math : "))
#     DE = int(input("Enter paper marks of design engineering : "))
#     c = int(input("Enter paper marks of c language : "))
#     english = int(input("Enter paper marks of english : "))

# class PractMarks:      # class-2
#     cpract = int(input("Enter practical marks of c language : "))

# class Result(SubMarks, PractMarks):      # child class
#     def total(self):
#         if self.math >= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cpract >= 20:
#             print("Pass")
#         else:
#             print("Fail")

# obj = Result()
# obj.total()

#---------------------------- METHOD OVERRIDING --------------------------------#
# Method overloading is not supported into python
# class RBI:
#     def home_loan(self):
#         print("Home loan ROI = 8%")

#     def education_loan(self):
#         print("Education loan = 9%")

# class SBI(RBI):
#     def education_loan(self):
#         print("Education loan = 10%")

# obj = SBI()
# obj.education_loan()

#-------------------------- SUPER METHOD ----------------------------#
# we want to access parent class method then we will use super() method

# class RBI:
#     def home_loan(self):
#         print("Home loan ROI = 8%")

#     def education_loan(self):
#         print("Education loan = 9%")

# class SBI(RBI):
#     def education_loan(self):
#         super().education_loan()
#         print("Education loan = 10%")

# obj = SBI()
# obj.education_loan()

#--------------------------------------------------------------------------#

class RBI:
    def __init__(self):
        print("Parent class constructor")

class SBI(RBI):
    def __init__(self):
        print("Child class constructor")
        super().__init__

obj = SBI()
