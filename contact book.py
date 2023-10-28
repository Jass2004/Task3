txt = "Contact Book"
x = txt.center(40, " ")

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if results:
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self, search_term, updated_contact):
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                contact.name = updated_contact.name
                contact.phone = updated_contact.phone
                contact.email = updated_contact.email
                contact.address = updated_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            updated_name = input("Updated Name: ")
            updated_phone = input("Updated Phone: ")
            updated_email = input("Updated Email: ")
            updated_address = input("Updated Address: ")
            updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
            contact_book.update_contact(search_term, updated_contact)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
