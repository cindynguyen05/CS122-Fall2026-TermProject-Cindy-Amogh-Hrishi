"""Demonstrate classes"""

from expense_manager import ExpenseManager

manager = ExpenseManager()
manager.load_from_csv("sample_data.csv")

manager.display_expenses()