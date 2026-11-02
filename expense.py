"""To represent a purchase. keeping the details together
(ID, date, category, description, amount, and payment method)"""

from dataclasses import dataclass
from datetime import date

#define
@dataclass
class Expense:
    expense_id: int
    date: date
    category: str
    description: str
    amount: float
    payment_method: str

# called automatically when call print()
# print (expense) will give something like this
# 2026-01-10 | Food | Lunch | $14.25 | Debit Card
def __str__(self):
    return (
                f"{self.date} | {self.category} | {self.description} | "
                f"${self.amount:.2f} | {self.payment_method}"
            )