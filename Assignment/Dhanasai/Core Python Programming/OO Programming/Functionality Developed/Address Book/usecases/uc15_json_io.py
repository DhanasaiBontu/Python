from model.contact import Contact
from model.address_book import AddressBook
from storage.json_storage import save_to_json, read_from_json

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))

    save_to_json(my_book, "address_book.json")
    print("Saved to address_book.json")

    data = read_from_json("address_book.json")
    print("Loaded from JSON:")
    for c in data:
        print(c)

if __name__ == "__main__":
    main()
