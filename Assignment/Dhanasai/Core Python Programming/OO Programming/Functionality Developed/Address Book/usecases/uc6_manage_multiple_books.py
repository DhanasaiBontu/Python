from model.contact import Contact
from model.address_book import AddressBook

def main():
    system_books = {}

    # Create multiple address books
    friends_book = AddressBook("Friends")
    work_book = AddressBook("Work")
    
    system_books["Friends"] = friends_book
    system_books["Work"] = work_book

    # Add contacts to Friends
    friends_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))
    friends_book.add_contact(Contact("Alice", "Smith", "456 Avenue", "Los Angeles", "CA", "90001", "9876543210", "alice@example.com"))

    # Add contacts to Work
    work_book.add_contact(Contact("Bob", "Brown", "789 Road", "Chicago", "IL", "60001", "5555555555", "bob@example.com"))

    print("System Address Books:")
    for name, book in system_books.items():
        print(f"\nAddress Book: {name}")
        for c in book.contacts:
            print(c)

if __name__ == "__main__":
    main()
