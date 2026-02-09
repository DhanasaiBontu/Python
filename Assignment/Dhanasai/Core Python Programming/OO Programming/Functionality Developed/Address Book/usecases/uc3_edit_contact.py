from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))

    print("Before edit:")
    for c in my_book.contacts:
        print(c)

    my_book.edit_contact("John", "Doe", phone_number="1112223333", city="Boston")
    
    print("\nAfter edit:")
    for c in my_book.contacts:
        print(c)

if __name__ == "__main__":
    main()
