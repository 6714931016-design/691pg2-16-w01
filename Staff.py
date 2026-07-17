
from Tax import Tax


class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearIncome(self):
        return self.salary * 12

    def calculateTax(self, income):
        return Tax.calculateTax(income)

    def __str__(self):
        return (f"{self.name} - Annual Income: {self.yearIncome()} Baht "
                f"- Tax to Pay: {self.calculateTax()} Baht")