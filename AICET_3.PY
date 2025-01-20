import json
from datetime import datetime

# File to store expense data
data_file = "expenses.json"

# Load existing data or initialize an empty list
def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save data to the file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter the amount: "))
        description = input("Enter a brief description: ")
        print("Select a category:")
        categories = ["Food", "Transportation", "Entertainment", "Other"]
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        category_choice = int(input("Enter the number of the category: "))
        if category_choice < 1 or category_choice > len(categories):
            raise ValueError("Invalid category choice.")
        category = categories[category_choice - 1]

        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data = load_data()
        data.append(expense)
        save_data(data)

        print("Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# View all expenses
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return

    print("\nExpenses:")
    for idx, expense in enumerate(data, 1):
        print(f"{idx}. Amount: {expense['amount']}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Date: {expense['date']}")

# View expense summaries
def view_summary():
    data = load_data()
    if not data:
        print("No expenses found.")
        return

    total_expenses = sum(expense["amount"] for expense in data)
    category_totals = {}
    for expense in data:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nExpense Summary:")
    print(f"Total Expenses: {total_expenses}")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

# Main menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                view_summary()
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
