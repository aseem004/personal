# Expense Tracker

A simple command-line application built in Python to track personal expenses.
It lets you add, view, and analyze your spending, with everything saved
permanently to a CSV file.

## Features

- **Add an expense** — record the date, category, amount, and a note
- **View all expenses** — see every recorded expense in a table
- **View total spending** — get the sum of everything you've spent
- **View spending by category** — see subtotals per category, sorted highest first
- **Delete an expense** — remove any entry by its number
- **Persistent storage** — all data is saved to `expenses.csv`, so nothing is lost when you close the program

## How it works

The program is a menu-driven loop: it keeps showing options (1–6) and running
the matching function until the user chooses to exit. Data is stored using
Python's built-in `csv` module in `DictReader`/`DictWriter` form, meaning each
row in the file is treated as a dictionary like:

```python
{"date": "2026-09-15", "category": "Food", "amount": "250.0", "note": "Lunch"}
```

Key design choices:
- **CSV instead of a database** — simple, human-readable, and needs no extra
  libraries. Great for a first project; can be swapped for SQLite later.
- **Separation of concerns** — each menu action (add, view, delete, etc.) is
  its own function, which keeps the code organized and easy to extend.
- **Input validation** — the amount field keeps asking until a valid number
  is entered, so the program doesn't crash on bad input.

## Getting started

1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/expense-tracker.git
   cd expense-tracker
   ```
3. Run the program:
   ```bash
   python3 expense_tracker.py
   ```
4. Follow the on-screen menu to add and manage your expenses.

## Possible future improvements

- Switch storage from CSV to a SQLite database
- Add monthly/weekly spending summaries
- Add a budget limit with warnings when exceeded
- Build a simple GUI version using Tkinter

## Author

<your name here>
