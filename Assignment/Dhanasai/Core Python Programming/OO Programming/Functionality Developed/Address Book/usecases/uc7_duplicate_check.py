from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    contact1 = Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com")
    contact2 = Contact("John", "Doe", "999 Avenue", "Boston", "MA", "02101", "1112223333", "john2@example.com")

    my_book.add_contact(contact1)
    my_book.add_contact(contact2)  # Duplicate

    print("Contacts in Address Book:")
    for c in my_book.contacts:
        print(c)

if __name__ == "__main__":
    main()
