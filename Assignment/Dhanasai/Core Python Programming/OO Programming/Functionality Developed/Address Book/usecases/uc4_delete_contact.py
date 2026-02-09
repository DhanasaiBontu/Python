from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))
    my_book.add_contact(Contact("Alice", "Smith", "456 Avenue", "Los Angeles", "CA", "90001", "9876543210", "alice@example.com"))

    print("Before delete:")
    for c in my_book.contacts:
        print(c)

    my_book.delete_contact("Alice", "Smith")
    
    print("\nAfter delete:")
    for c in my_book.contacts:
        print(c)

if __name__ == "__main__":
    main()
