import csv
import random
from datetime import date, timedelta

random.seed(42)

expense_options = {
    "Food": [
        ("Lunch", 8, 30),
        ("Dinner", 15, 60),
        ("Coffee", 3, 10),
    ],
    "Entertainment": [
        ("Movies", 12, 30),
        ("Concert", 30, 150),
        ("Video game", 20, 70),
    ],
    "Groceries": [
        ("Weekly groceries", 30, 150),
        ("Household supplies", 10, 80),
    ],
    "Transportation": [
        ("Gas", 25, 80),
        ("Bus fare", 2, 15),
        ("Rideshare", 8, 50),
    ],
}

payment_methods = [
    "Credit Card",
    "Debit Card",
    "Cash",
    "Other",
]

start_date = date(2026, 1, 1)
end_date = date(2026, 12, 31)
date_range = (end_date - start_date).days

number_of_expenses = 200
expenses = []

for expense_id in range(1, number_of_expenses + 1):
    category = random.choice(list(expense_options))
    description, minimum, maximum = random.choice(
        expense_options[category]
    )

    expense_date = start_date + timedelta(
        days=random.randint(0, date_range)
    )

    expenses.append({
        "expense_id": expense_id,
        "date": expense_date.isoformat(),
        "category": category,
        "description": description,
        "amount": round(random.uniform(minimum, maximum), 2),
        "payment_method": random.choice(payment_methods),
    })

with open("sample_data.csv", "w", newline="") as file:
    fieldnames = [
        "expense_id",
        "date",
        "category",
        "description",
        "amount",
        "payment_method",
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expenses)

print(f"Generated {number_of_expenses} expenses.")