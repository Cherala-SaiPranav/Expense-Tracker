import csv
from datetime import datetime

csv_file = "Expense.csv"

def initialize_csv():
    try:
        with open(csv_file, mode='x', newline='') as file:
            csv.writer(file).writerow(["Date", "Category", "Amount", "Type"])
    except FileExistsError:
        pass

def addExpense(Date, Category, Amount, Type):
    with open(csv_file, mode='a', newline='') as file:
        csv.writer(file).writerow([Date, Category, Amount, Type])
    print("Expense added successfully!")

def viewExpenses():
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # Skipping the header
        for row in reader:
            print(row)

def main():

    initialize_csv()

    while True:
        print("--- Expense Tracker ---")
        print("1. Add Expense/Income")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            while True:
                Date = input("Enter date(YYYY-MM-DD): ")
                try:
                    datetime.strptime(Date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            Category = input("Enter category (example: Food, Travel): ")

            while True:
                try:
                    Amount = float(input("Enter amount: "))
                    break
                except ValueError:
                    print("Please enter a valid amount.")

            while True:
                Type = input("Enter type (income/expense): ").strip().lower()
                if Type in ['income', 'expense']:
                    break
                else:
                    print("Invalid type. Please enter 'income' or 'expense'.")
            addExpense(Date, Category, Amount, Type)

        elif choice == "2":
            viewExpenses()

        elif choice == "3":
            break

        else:
            print("Invalid Choice. Please try again.")

main()