import json

def add_expense(amount, category):
    data = {"amount": amount, "category": category}

    try:
        with open("data.json", "r") as f:
            expenses = json.load(f)
    except:
        expenses = []

    expenses.append(data)

    with open("data.json", "w") as f:
        json.dump(expenses, f)


def show_expenses():
    try:
        with open("data.json", "r") as f:
            expenses = json.load(f)
            for e in expenses:
                print(e["amount"], "-", e["category"])
    except:
        print("No expenses yet")


def total_expense():
    try:
        with open("data.json", "r") as f:
            expenses = json.load(f)
            total = sum(int(e["amount"]) for e in expenses)
            print("Total:", total)
    except:
        print("No data")