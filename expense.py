"""To represent a purchase. keeping the details together
(ID, date, category, description, amount, and payment method)"""

from dataclasses import dataclass
from datetime import date

from validation import (
    validate_amount,
    validate_date,
    validate_expense_id,
    validate_text,
)

#define
@dataclass
class Expense:
    expense_id: int
    date: date
    category: str
    description: str
    amount: float
    payment_method: str

    def __post_init__(self):
        self.expense_id = validate_expense_id(self.expense_id)
        self.date = validate_date(self.date)
        self.category = validate_text(self.category, "Category")
        self.description = validate_text(self.description, "Description")
        self.amount = validate_amount(self.amount)
        self.payment_method = validate_text(
            self.payment_method, "Payment method"
        )

    # Called automatically when print(expense) is used.
    def __str__(self):
        return (
            f"{self.date} | {self.category} | {self.description} | "
            f"${self.amount:.2f} | {self.payment_method}"
        )
