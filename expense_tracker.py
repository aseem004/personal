"""
Expense Tracker
----------------
A simple command-line application to record, view, and analyze personal expenses.
Data is stored permanently in a CSV file (expenses.csv) so it survives
between program runs.

Author: <your name here>
"""

import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"
FIELDNAMES = ["date", "category", "amount", "note"]


def initialize_file():
    """
    Make sure the CSV file exists and has a header row.
    This runs once every time the program starts.
    """
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_expenses():
    """
    Read all expenses from the CSV file and return them as a list of
    dictionaries, e.g. [{"date": "...", "category": "...", ...}, ...]
    """
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_all_expenses(expenses):
    """
    Overwrite the CSV file with the given list of expense dictionaries.
    Used after deleting an expense, since we rewrite the whole file.
    """
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense():
    """
    Ask the user for expense details and append a new row to the CSV file.
    """
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input == "":
        date_input = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (e.g. Food, Transport, Rent): ").strip().title()

    # Keep asking until the user gives a valid number for amount
    while True:
        amount_input = input("Enter amount spent: ").strip()
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("That's not a valid number. Try again.")

    note = input("Enter a short note (optional): ").strip()

    new_expense = {
        "date": date_input,
        "category": category,
        "amount": amount,
        "note": note,
    }

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(new_expense)

    print(f"Added: {category} - {amount} on {date_input}\n")


def view_expenses():
    """
    Print every expense currently stored, in a readable table format.
    """
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print(f"\n{'No.':<5}{'Date':<12}{'Category':<15}{'Amount':<10}{'Note'}")
    print("-" * 55)
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}{expense['date']:<12}{expense['category']:<15}"
            f"{expense['amount']:<10}{expense['note']}"
        )
    print()


def view_total():
    """
    Calculate and print the sum of all recorded expenses.
    """
    expenses = load_expenses()
    total = sum(float(expense["amount"]) for expense in expenses)
    print(f"Total spending: {total:.2f}\n")


def view_by_category():
    """
    Group expenses by category and print the subtotal for each one.
    """
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.\n")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        totals[category] = totals.get(category, 0) + amount

    print("\nSpending by category:")
    for category, total in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        print(f"  {category:<15}{total:.2f}")
    print()


def delete_expense():
    """
    Show all expenses with numbers, then let the user pick one to delete.
    """
    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete.\n")
        return

    view_expenses()
    choice = input("Enter the number of the expense to delete (or 0 to cancel): ").strip()

    if not choice.isdigit():
        print("Invalid input.\n")
        return

    choice = int(choice)
    if choice == 0:
        print("Cancelled.\n")
        return

    if 1 <= choice <= len(expenses):
        removed = expenses.pop(choice - 1)
        save_all_expenses(expenses)
        print(f"Deleted: {removed['category']} - {removed['amount']}\n")
    else:
        print("Number out of range.\n")


def print_menu():
    print("=" * 35)
    print("        EXPENSE TRACKER")
    print("=" * 35)
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Delete an expense")
    print("6. Exit")


def main():
    """
    The main program loop. Keeps showing the menu until the user chooses
    to exit.
    """
    initialize_file()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
