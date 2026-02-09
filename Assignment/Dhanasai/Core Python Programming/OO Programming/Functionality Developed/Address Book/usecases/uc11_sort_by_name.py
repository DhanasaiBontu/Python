from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("Charlie", "Brown", "123 St", "NY", "NY", "10001", "123", "c@example.com"))
    my_book.add_contact(Contact("Alice", "Smith", "456 Ave", "LA", "CA", "90001", "456", "a@example.com"))
    my_book.add_contact(Contact("Bob", "Doe", "789 Rd", "Chicago", "IL", "60001", "789", "b@example.com"))

    my_book.sort_by_attribute("first_name")
    print("Contacts sorted by first name:")
    for c in my_book.contacts:
        print(c)

if __name__ == "__main__":
    main()
