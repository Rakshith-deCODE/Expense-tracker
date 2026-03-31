from database import add_expense, show_expenses, total_expense

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        add_expense(amount, category)

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        break