"""Validation helpers for expense records.

Keeping validation in one file makes it reusable for the future Flask forms
and prevents invalid values from entering the manager.
"""

import math
import re
from datetime import date


class ExpenseValidationError(ValueError):
    """Raised when an expense field has an invalid value."""


DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TEXT_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 &'()\-/]*$")


def validate_expense_id(expense_id):
    if isinstance(expense_id, bool) or not isinstance(expense_id, int):
        raise ExpenseValidationError("Expense ID must be a whole number.")
    if expense_id <= 0:
        raise ExpenseValidationError("Expense ID must be greater than zero.")
    return expense_id


def validate_date(expense_date):
    if isinstance(expense_date, str):
        if not DATE_PATTERN.fullmatch(expense_date):
            raise ExpenseValidationError("Date must use YYYY-MM-DD format.")
        try:
            expense_date = date.fromisoformat(expense_date)
        except ValueError as exc:
            raise ExpenseValidationError("Date is not valid.") from exc

    if not isinstance(expense_date, date):
        raise ExpenseValidationError("Date must be a date or YYYY-MM-DD string.")
    return expense_date


def validate_text(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ExpenseValidationError(f"{field_name} cannot be empty.")
    value = value.strip()
    if not TEXT_PATTERN.fullmatch(value):
        raise ExpenseValidationError(
            f"{field_name} contains unsupported characters."
        )
    return value


def validate_amount(amount):
    try:
        amount = float(amount)
    except (TypeError, ValueError) as exc:
        raise ExpenseValidationError("Amount must be a number.") from exc

    if not math.isfinite(amount) or amount <= 0:
        raise ExpenseValidationError("Amount must be greater than zero.")
    if round(amount, 2) != amount:
        raise ExpenseValidationError("Amount cannot have more than two decimals.")
    return amount
