from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    contact = Contact("Alice", "Smith", "456 Avenue", "Los Angeles", "CA", "90001", "9876543210", "alice@example.com")
    my_book.add_contact(contact)
    print("Contact added:")
    for c in my_book.contacts:
        print(c)

if __name__ == "__main__":
    main()
