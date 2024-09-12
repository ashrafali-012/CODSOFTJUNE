contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}")

# Function to search for a contact by name or phone
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['Name'] or search_term in contact['Phone']]
    
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
    else:
        print("No contact found with that name or phone number.")

# Function to update an existing contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['Name'] == name:
            print(f"Updating contact: {contact['Name']}")
            contact['Phone'] = input(f"Enter new phone number (current: {contact['Phone']}): ") or contact['Phone']
            contact['Email'] = input(f"Enter new email (current: {contact['Email']}): ") or contact['Email']
            contact['Address'] = input(f"Enter new address (current: {contact['Address']}): ") or contact['Address']
            print("Contact updated successfully!")
            return
    print("Contact not found!")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact['Name'] != name]
    print(f"Contact '{name}' deleted successfully!")

# Main function to handle user interface
def contact_book():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the contact book
contact_book()
