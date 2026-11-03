"""Keeps track of multiple expenses"""

import csv
from datetime import date
from expense import Expense
from validation import ExpenseValidationError


class ExpenseDataError(Exception):
    """Raised when the CSV file cannot be read as expense data."""

class ExpenseManager:
    """Stores expenses and provides basic ways to manage"""

    def __init__(self):
        # a list that starts empty and will hold Expense objects
        self.expenses = []

    # adds an expense
    def add_expense(self, expense):
        if not isinstance(expense, Expense):
            raise TypeError("Only Expense objects can be added.")
        if any(existing.expense_id == expense.expense_id
               for existing in self.expenses):
            raise ExpenseValidationError(
                f"Expense ID {expense.expense_id} already exists."
            )
        self.expenses.append(expense)

    #displays expense in collection
    def display_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return

        for expense in self.expenses:
            print(expense)

    #returns list of expenses
    def get_all_expenses(self):
        return self.expenses

    # returns sum of all expenses
    def total_spending(self):
        return sum(expense.amount for expense in self.expenses)

    # reads expenses from file and adds to collection
    def load_from_csv(self, filename):
        try:
            with open(filename, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                required_columns = {
                    "expense_id", "date", "category", "description",
                    "amount", "payment_method",
                }
                if not required_columns.issubset(reader.fieldnames or []):
                    raise ExpenseDataError("CSV file is missing required columns.")

                for row_number, row in enumerate(reader, start=2):
                    try:
                        expense = Expense(
                            expense_id=int(row["expense_id"]),
                            date=date.fromisoformat(row["date"]),
                            category=row["category"],
                            description=row["description"],
                            amount=float(row["amount"]),
                            payment_method=row["payment_method"],
                        )
                        self.add_expense(expense)
                    except (ValueError, TypeError, ExpenseValidationError) as exc:
                        raise ExpenseDataError(
                            f"Invalid expense on CSV row {row_number}: {exc}"
                        ) from exc
        except FileNotFoundError as exc:
            raise ExpenseDataError(f"Could not find CSV file: {filename}") from exc
        except OSError as exc:
            raise ExpenseDataError(f"Could not read CSV file: {exc}") from exc
