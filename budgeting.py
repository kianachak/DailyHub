bills = {}

def main():
    print("=======================")
    print("      <Budgeting>      ")
    menu_options = ["Add Bills", "Show Bills", "Weekly Report", "Edit Bills", "Quit"]

    while True:
        print("=======================")
        for index, option in enumerate(menu_options):
            print(f"{index}. {option}")

        menu = input("What is your option:: ")
        if menu == "add bills" or menu == "0":
            add_bill()
        elif menu == "show bills" or menu == "1":
            show_bills()
        elif menu == "weekly report" or menu == "2":
            weekly_report()
        elif menu == "edit bills" or menu == "3":
            edit_bill()
        elif menu == "quit" or menu == "4":
            print("\nSee you later.")
            break
        else:
            print("\nInvalid input.")


def add_bill():
    new_bill = input("Enter the name of bill: ")
    while True:
        if new_bill in bills:
            print("\nThis bill is already added. do you want to edit this one or just a mistake? ")
            mistake = input("Enter if you want to edit it. Enter add bill if you want a new try: ")
            if mistake == "":
                name_bill = new_bill
                edit_bill(name_bill)
                return name_bill
            elif mistake == "add bill":
                new_bill = input("Enter the name of bill again: ")
            else:
                return
        else:
            break
    while True:
        try:
            amount = int(input(f'Enter the amount of {new_bill}: '))
            break
        except ValueError:
            print("\nAmount should be integer.")

    while True:
        try:
            due_date = int(input(f'Enter the due date of {new_bill}: '))
            if 1 <= due_date <= 31:
                break
            else:
                print ("\nDue date must be between 1 and 31.")
        except ValueError:
            print("\ndue date should be integer.")

    bills[new_bill] = [amount, due_date]
    date = bills[new_bill][1]
    return date

def format_due_date(date):
    if date == 1 or date == 21 or date == 31:
        return f'{date}st'
    elif date == 2 or date == 22:
        return f'{date}nd'
    elif date == 3 or date == 23:
        return f'{date}rd'
    else:
        return f'{date}th'

def show_bills():
    if not bills:
        print("\nYour budget table is empty.")
    else:
        print(f'{"Bill":<12}{"Amount":<12}{"Due Date":<10}')
        for bill_name in bills:
            print(f'{bill_name:<12}{bills[bill_name][0]:<12}{format_due_date(bills[bill_name][1]):<10}')


def weekly_report():
    weeks = [
        (1, 7),
        (8, 14),
        (15, 21),
        (22, 28),
        (29, 31)
    ]

    for number, (start, end) in enumerate(weeks):
        week = ["First", "Second", "Third", "Fourth", "Fifth"]
        print(f'                 {week[number]} Week')
        print(f'{"Bill":<12}{"Amount":<12}{"Due Date":<10}')
        weekly_amounts = []
        for bill_name in bills:
            due_date = bills[bill_name][1]
            if start <= due_date <= end:
                print(f'{bill_name:<12}{bills[bill_name][0]:<12}{format_due_date(bills[bill_name][1]):<10}')
                weekly_amounts.append(bills[bill_name][0])

        print("----------------------------------")
        print(f'Total: {sum(weekly_amounts)}')

def edit_bill(name_bill=None):
    if not name_bill:  
        name_bill = input("Enter your bill's name: ")
        if name_bill not in bills:
            print("\nThis bill does not exist.")
            return

    edit = input(f'Which part of {name_bill}, you want to edit? (amount or due date)')
    if edit == "amount":
        try:
            new_amount = int(input("Enter your new amount. "))
            if new_amount == bills[name_bill][0]:
                print("\nYour amount is the same.")
                return
            else:
                bills[name_bill][0] = new_amount
        except ValueError:
            print("\nAmount should be integer.")
        

    elif edit == "due date":
        try:
            new_due_date = int(input("Enter your new due date. "))
            if 1 <= new_due_date <= 31:
                if new_due_date == bills[name_bill][1]:
                    print("\nYour due date is the same.")
                    return
                else:
                    bills[name_bill][1] = new_due_date
            else:
                print ("\nDue date must be between 1 and 31.")
        except ValueError:
            print("\nDue date should be integer.")

    else:
        print("\ninvalid option. try again")
        return
