import todo
import notes
import expenses
import budgeting

print("============================")
print("  Wellcome To DailyHub  ")
print("============================")
menu_options = ["To Do List", "Notes", "Expenses", "Budgeting", "Quit"]

def main():
    while True:
        print("======================")
        for index, option in enumerate(menu_options):
            print(f"{index}. {option}")

        menu = input("Which place you want to go?: ").lower()
        if menu == "to do list" or menu == "0":
            todo.main()
        elif menu == "notes" or menu == "1":
            notes.main()
        elif menu == "expenses" or menu == "2":
            expenses.main()
        elif menu == "budgeting" or menu == "3":
            budgeting.main()
        elif menu == "quit" or menu == "4":
            print("See you later.")
            break
        else:
            print("Invalid option.")

main()