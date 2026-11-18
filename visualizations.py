"""Create spending charts from a list of Expense objects."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def expenses_to_dataframe(expenses):
    """Convert Expense objects into a DataFrame for analysis and charting."""
    rows = [
        {
            "date": expense.date,
            "category": expense.category,
            "amount": expense.amount,
            "payment_method": expense.payment_method,
        }
        for expense in expenses
    ]
    dataframe = pd.DataFrame(rows)
    if not dataframe.empty:
        dataframe["date"] = pd.to_datetime(dataframe["date"])
    return dataframe


def create_spending_visualizations(expenses, output_folder="charts"):
    """Save category and monthly spending charts and return their paths."""
    dataframe = expenses_to_dataframe(expenses)
    if dataframe.empty:
        raise ValueError("At least one expense is needed to create charts.")

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    category_totals = (
        dataframe.groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )
    category_chart = output_folder / "spending_by_category.png"
    plt.figure(figsize=(8, 5))
    sns.barplot(
        category_totals,
        x="amount",
        y="category",
        hue="category",
        legend=False,
        palette="viridis",
    )
    plt.title("Total Spending by Category")
    plt.xlabel("Amount ($)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(category_chart, dpi=150)
    plt.close()

    monthly_totals = (
        dataframe.assign(month=dataframe["date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)["amount"]
        .sum()
    )
    monthly_chart = output_folder / "spending_by_month.png"
    plt.figure(figsize=(10, 5))
    sns.lineplot(
        monthly_totals,
        x="month",
        y="amount",
        marker="o",
        color="teal",
    )
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(monthly_chart, dpi=150)
    plt.close()

    return category_chart, monthly_chart
