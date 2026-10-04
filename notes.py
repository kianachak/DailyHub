notes = []

def main():
    print("=======================")
    print("        <Notes>        ")
    menu_options = ["Add Notes", "Show Notes", "Delete Notes", "Search Notes", "Edit Notes", "Quit"]

    while True:
        print("=======================")
        for index, option in enumerate(menu_options):
            print(f"{index}. {option}")

        menu = input("What is your option: ").lower()
        if menu == "add notes" or menu == "0":
            add_note()
        elif menu == "show notes" or menu == "1":
            show_note()
        elif menu == "delete notes" or menu == "2":
            delete_note()
        elif menu == "search notes" or menu == "3":
            search_note()
        elif menu == "edit notes" or menu == "4":
            edit_note()
        elif menu == "quit" or menu == "5":
            print("\nSee you later.")
            break
        else:
            print("\nInvalid input.")

def add_note():
    new_note = input("Please enter your note: ")
    if new_note == "":
        print("\nWrite your note again.")
        return
    if new_note in notes:
        print("\nThis note already exists.")
    else:
        notes.append(new_note)
        print("\nNote added successfully.")

def show_note():
    if not notes:
        print("\nThe Notes are empty.")
    else:
        for index, note in enumerate(notes):
            print(f'\n{index}. {note}')

def delete_note():
    if not notes:
        print("\nYour notes are empty.")
    else:
        note_name = input("\nWhich note you wish to delete it? ")
        if note_name in notes:
            notes.remove(note_name)
            print(f'\n{note_name} has removed from your notes. ')
        else:
            print("\nYour note doesn't exist.")
    
def search_note():
    if not notes:
        print("\nYour notes are empty.")
    else:
        found = False
        search = input("Write your search note here: ")
        for note in notes:
            if search in note:
                found = True      
                print("\nfound! ")
                print(f'{note}')    
        if not found:
            print("\nYour search doesn't exist.")

def edit_note():
    if not notes:
        print("\nYour notes are empty.")
    else:
        note_name = input("Which note you want to edit? ")
        if note_name in notes:
            new_note_name = input("What is your edited note? ")
            if new_note_name == "":
                print("\nPlease write your note again.")
                return
            elif new_note_name in notes:
                print("\nThis note already exists.")
                return
            else:
                for index, note in enumerate(notes):
                    if note == note_name:
                        notes[index] = new_note_name
                        print("\nNote edited successfully.") 
        else:
            print("\nYour note doesn't exist.")
