expense = {}

def main():
    print("=======================")
    print("       <ٍExpenses>      ")
    menu_options = ['Add Expense', 'Show Expenses', 'Total Spending', 'Quit']

    while True:
        print("=======================")
        for index, option in enumerate(menu_options):
            print(f"{index}. {option}")

        menu = input("What is your option: ").lower()
        if menu == "add expense" or menu == "0":
            add_expense()
        elif menu == "show expenses" or menu == "1":
            show_expense()
        elif menu == "total spending" or menu == "2":
            total_spending()
        elif menu == "quit" or menu == "3":
            print("\nSee you later.")
            break
        else:
            print("\nInvalid input.")

def process_spend(new_expense):
    while True:
        try:
            new_spend = int(input(f'Enter the spend of {new_expense}: '))
            if new_spend < 0:
                print("\nYour spend can't be nagetive.")
            else:
                if new_expense in expense:
                    total_spend = expense[new_expense] + new_spend
                    expense[new_expense] = total_spend
                    break
                else:
                    expense[new_expense] = new_spend
                    break
        except ValueError:
            print("\nPlease enter a valid number.")

def add_expense():
    while True:
        new_expense = input("Enter your expense name: ")
        if new_expense == "":
            print("\nPlease enter an expense name.")
            continue
        else:
            process_spend(new_expense)
            print("\nYour new expense has been added.")
            break
        
def show_expense():
    if not expense:
        print("\nYour expenses are empty.")
    else:
        for kv in expense: 
            print(f'{kv}: {expense[kv]}')

def total_spending():
    if not expense:
        print("\nNo expenses yet.")
    else:
        total = sum(expense.values())
        print(f'\nThe total of all this expenses are: {total}')
   