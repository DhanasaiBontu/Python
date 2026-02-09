from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")

    contacts = [
        Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"),
        Contact("Alice", "Smith", "456 Avenue", "Los Angeles", "CA", "90001", "9876543210", "alice@example.com"),
        Contact("Bob", "Brown", "789 Road", "Chicago", "IL", "60001", "5555555555", "bob@example.com")
    ]

    for contact in contacts:
        my_book.add_contact(contact)

    print("All contacts:")
    for c in my_book.contacts:
        print(c)

if __name__ == "__main__":
    main()
