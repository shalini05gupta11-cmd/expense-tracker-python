# Expense Tracker - Easy Version

file_name = "expenses.txt"

def add_expense():
    date = input("Enter date: ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")

    file = open(file_name, "a")
    file.write(date + "," + category + "," + amount + "\n")
    file.close()

    print("Expense saved!\n")


def view_expenses():
    print("\nDate | Category | Amount")
    print("-------------------------")

    try:
        file = open(file_name, "r")
        for line in file:
            print(line.strip())
        file.close()
    except:
        print("No data found\n")


def total_expense():
    total = 0

    try:
        file = open(file_name, "r")
        for line in file:
            amount = line.strip().split(",")[2]
            total = total + float(amount)
        file.close()

        print("Total Expense =", total, "\n")
    except:
        print("No data found\n")


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Bye 👋")
        break
    else:
        print("Wrong choice\n")
