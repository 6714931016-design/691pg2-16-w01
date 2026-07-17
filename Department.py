
from Tax import Tax
from Staff import Staff


class Department:
    def __init__(self, name=None):
        self.name = name
        self.staffs = []

    def addStaff(self, staff):
        self.staffs.append(staff)

    def calculateTotals(self):
        total_income = 0
        total_tax = 0

        for staff in self.staffs:
            income = staff.yearIncome()
            tax = staff.calculateTax(income)

            total_income += income
            total_tax += tax

        return total_income, total_tax

    def displayResults(self):
        if self.name:
            print(f"Department: {self.name}")

        print("Staff Information")
        for staff in self.staffs:
            income = staff.yearIncome()
            tax = staff.calculateTax(income)
            print(f"{staff.name} - Annual Income: {income} Baht - Tax to Pay: {tax} Baht")

        total_income, total_tax = self.calculateTotals()

        if len(self.staffs) > 0:
            average_income = total_income / len(self.staffs)
            average_tax = total_tax / len(self.staffs)
        else:
            average_income = 0
            average_tax = 0

        print("-" * 40)
        print(f"Total Income   : {total_income} Baht")
        print(f"Average Income : {average_income:.2f} Baht")
        print(f"Total Tax      : {total_tax} Baht")
        print(f"Average Tax    : {average_tax:.2f} Baht")