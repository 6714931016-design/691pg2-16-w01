from Tax import Tax
from Staff import Staff
from Department import Department

staff1 = Staff("Alex", 45000)
staff2 = Staff("Michael", 60000)
staff3 = Staff("Charlie", 87000)
staff4 = Staff("Dylan", 100000)
staff5 = Staff("Joe", 150000)

dept = Department("IT")

dept.addStaff(staff1)
dept.addStaff(staff2)
dept.addStaff(staff3)
dept.addStaff(staff4)
dept.addStaff(staff5)

dept.displayResults()