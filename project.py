import pandas as pd

# DataFrames initialization
incomes = pd.DataFrame(columns=['Amount', 'Source', 'Month', 'Category'])
expenses = pd.DataFrame(columns=['Amount', 'Category', 'Month'])

def add_record(df, record_type):
    while True:
        try:
            amount = float(input(f"Enter {record_type} amount: $"))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        while True:
            category = input(f"Enter {record_type} category (Mobile/Automotive/Service): ")
            if category not in ['Mobile', 'Automotive', 'Service']:
                print("Invalid Category. Please try again.")
            else:
                break

        while True:
            try:
                month = int(input(f"Enter {record_type} month (1-12): "))
                if month < 1 or month > 12:
                    raise ValueError
                break
            except ValueError:
                print("Invalid month. Please enter a number between 1 and 12.")

        source = input(f"Enter {record_type} source: ") if record_type == 'income' else None
        new_index = len(df)
        df.loc[new_index] = [amount, source, month, category] if record_type == 'income' else [amount, category, month]

        if input(f"Add more {record_type}? (y/n): ") != 'y':
            break

def add_income():
    global incomes
    add_record(incomes, 'income')

def add_expense():
    global expenses
    add_record(expenses, 'expense')

def generate_report():

    # Overall summary
    total_income = incomes['Amount'].sum()
    total_expense = expenses['Amount'].sum()
    net_profit = total_income - total_expense
    net_profit_percentage = (net_profit / total_income * 100) if total_income else 0
    print("\nOverall Summary:")
    print(f"Total Income: ${total_income:,.2f}")
    print(f"Total Expense: ${total_expense:,.2f}")
    print(f"Net Profit: ${net_profit:,.2f}")
    print(f"Net Profit(%): {net_profit_percentage:.2f}%")

    # Income Report and Expense Report
    sorted_incomes = incomes.sort_values(by=['Month', 'Category', 'Amount'], ascending=True)
    sorted_expenses = expenses.sort_values(by=['Month', 'Category', 'Amount'], ascending=True)

    print("\nIncome Report:")
    print(sorted_incomes.to_string(index=False, formatters={'Amount':'${:,.2f}'.format}))
    print("\nExpense Report:")
    print(sorted_expenses.to_string(index=False, formatters={'Amount':'${:,.2f}'.format}))

    # Category-wise Profit summary
    print("\nCategory-wise Profit(%) Summary:")
    for category in ['Mobile', 'Automotive', 'Service']:
        category_income = incomes[incomes['Category'] == category]['Amount'].sum()
        category_expense = expenses[expenses['Category'] == category]['Amount'].sum()
        category_profit = category_income - category_expense
        profit_rate = (category_profit / category_income * 100) if category_income > 0 else 0
        print(f"{category}: Profit = ${category_profit:,.2f} ({profit_rate:.2f}%)")
    
    # Monthly summary
    print("\nMonthly Summary:")
    months = range(1, 13)
    for month in months:
        month_income = incomes[incomes['Month'] == month]['Amount'].sum()
        month_expense = expenses[expenses['Month'] == month]['Amount'].sum()
        month_profit = month_income - month_expense
        profit_rate = (month_profit / month_income * 100) if month_income > 0 else 0
        print(f"Month {month}:  Income = ${month_income:,.2f}, Expense = ${month_expense:,.2f}, Profit = ${month_profit:,.2f}, Rate = {profit_rate:.2f}%")



def main():
    while True:
        print("\nWelcome to the Profit Management System")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()