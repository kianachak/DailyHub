tasks = {}

def main():
    print("======================")
    print("     <To-Do List>     ")
    menu_options = ["Add", "Remove", "Show", "Finish task", "Quit"]

    while True:
        print("======================")
        for index, option in enumerate(menu_options):
            print(f"{index}. {option}")

        menu = input("What is your option: ")
        if menu == "add" or menu == "0":
            add_task()
        elif menu == "remove" or menu == "1":
            remove_task()
        elif menu == "show" or menu == "2":
            show_task()
        elif menu == "finish task" or menu == "3":
            finish_task()
        elif menu == "quit" or menu == "4":
            print("\nSee you later.")
            break
        else:
            print("\nInvalid input.")


def add_task():
    new_task = input("Enter your task: ")
    if new_task == "":
        print("\nPlease enter your task.")
        return
    if new_task in tasks:
        print("\nYou already added this task.")
    else:
        tasks[new_task] = "Not Done"
        print("\nTask added successfully.")


def remove_task():
    task_name = input("Which task do you want to remove? ")
    if task_name in tasks:
        del tasks[task_name]
        print(f'\nTask "{task_name}" removed.')
    else:
        print(f'\nTask "{task_name}" was not found.')


def show_task():
    if not tasks:
        print("\nThe list of your tasks is empty.")
    else:
        for index, task_name in enumerate(tasks):
            print(f'\n{index} --> {task_name} --> {tasks[task_name]}')


def finish_task():
    task_name = input("Which task have you finished? ")
    if task_name in tasks:
        if tasks[task_name] == "Done":
            print("\nYou already finished this task.")
            return
        else:
            tasks[task_name] = "Done"
            print("\nWell done.")
    else:
        print("\nTask was not found.")

