import pickle  # For saving and loading contacts

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            contact = get_contact_details()
            contacts.append(contact)
            save_contacts(contacts)
            print("Contact added successfully!")
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def get_contact_details():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    return {'name': name, 'phone': phone, 'email': email}

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the index of the contact you want to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = get_contact_details()
            contacts[index] = contact
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid index. Please select a valid contact.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the index of the contact you want to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"{deleted_contact['name']} has been deleted from the contacts.")
        else:
            print("Invalid index. Please select a valid contact.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def save_contacts(contacts):
    with open('contacts.pkl', 'wb') as file:
        pickle.dump(contacts, file)

def load_contacts():
    try:
        with open('contacts.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main":
  main()
