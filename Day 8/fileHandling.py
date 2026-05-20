#-------------------- FILE HANDLING --------------------------#

# import csv
# f = open("employee.csv",'a')
# a = csv.writer(f)
# #a.writerow(["EmpID" , "Emp name" , "Emp age"])
# empid = int(input("Enter employee id: "))
# empName = input("Enter employee name: ")
# empAge = int(input("Enter employee age: "))
# a.writerow([empid , empName , empAge])
# print("File has created")

#----------------------------------------------------------------------#

"""
col name = studId, studName, phy, chem, math, Total, Percentage, Result

input : studid, studname, phy, chem, math
calculate : total, percentage
check condition all paper marks >= 40 pass else fail

"""

import csv
f = open("student.csv", 'a')
a = csv.writer(f)
#a.writerow(["studID", "studName", "phy", "chem", "maths", "total", "percentage"])
studID = int(input("Enter the studID :"))
studName = input("Enter the studName :")
phy = int(input("Enter the Phy :"))
chem = int(input("Enter the Chem :"))
maths = int(input("Enter the Maths :"))
total = phy+chem+maths
percent = (total/300)*100
a.writerow([studID,studName,phy,chem,maths,total,percent])
print("File has been created")