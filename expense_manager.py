"""Keeps track of multiple expenses"""

import csv
from datetime import date
from expense import Expense

class ExpenseManager:
    def __init__(self):
        # a list that starts empty and will hold Expense objects
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def display_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return

        for expense in self.expenses:
            print(expense)

    def get_all_expenses(self):
        return self.expenses

    def load_from_csv(self, filename):
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = Expense(
                    expense_id=int(row["expense_id"]),
                    date=date.fromisoformat(row["date"]),
                    category=row["category"],
                    description=row["description"],
                    amount=float(row["amount"]),
                    payment_method=row["payment_method"],
                )
                self.add_expense(expense)

        def total_spending(self):
            return sum(expense.amount for expense in self.expenses)