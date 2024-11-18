def addExpense():
    print("Add")

def viewExpenses():
    print("View")

def main():
    while True:
        print("--- Expense Tracker ---")
        print("1. Add Expense/Income")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            addExpense()

        elif choice == "2":
            viewExpenses()

        elif choice == "3":
            break

        else:
            print("Invalid Choice. Please try again.")

main()