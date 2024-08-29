def show_menu():
    print("\nContact Agenda")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Show contacts")
    print("5. Exit")

def add_contact(agenda):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    agenda[name] = phone
    print(f"Contact {name} added.")

def modify_contact(agenda):
    name = input("Enter the name of the contact to modify: ")
    if name in agenda:
        new_phone = input("Enter the new phone number: ")
        agenda[name] = new_phone
        print(f"Contact {name} modified.")
    else:
        print("Contact does not exist.")

def delete_contact(agenda):
    name = input("Enter the name of the contact to delete: ")
    if name in agenda:
        del agenda[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact does not exist.")

def show_contacts(agenda):
    if agenda:
        print("\nContact List:")
        for name, phone in agenda.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("The agenda is empty.")

def main():
    agenda = {}
    while True:
        show_menu()
        option = input("Select an option (1-5): ")
        if option == '1':
            add_contact(agenda)
        elif option == '2':
            modify_contact(agenda)
        elif option == '3':
            delete_contact(agenda)
        elif option == '4':
            show_contacts(agenda)
        elif option == '5':
            print("Exiting the agenda...")
            break
        else:
            print("Invalid option, please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
