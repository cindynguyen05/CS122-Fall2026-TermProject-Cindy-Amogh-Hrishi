"""Demonstrate classes"""

from expense_manager import ExpenseManager
from expense_manager import ExpenseDataError
from visualizations import create_spending_visualizations


def main():
    manager = ExpenseManager()
    try:
        manager.load_from_csv("sample_data.csv")
        manager.display_expenses()
        category_chart, monthly_chart = create_spending_visualizations(
            manager.get_all_expenses()
        )
        print(f"\nCharts saved to {category_chart} and {monthly_chart}.")
    except ExpenseDataError as error:
        print(f"Error loading expenses: {error}")
    except ValueError as error:
        print(f"Error creating charts: {error}")


if __name__ == "__main__":
    main()
