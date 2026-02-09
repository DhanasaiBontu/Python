from model.contact import Contact
from model.address_book import AddressBook
from storage.file_storage import save_to_file, read_from_file

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))
    
    save_to_file(my_book, "address_book.txt")
    print("Saved to address_book.txt")

    lines = read_from_file("address_book.txt")
    print("Loaded from file:")
    for line in lines:
        print(line.strip())

if __name__ == "__main__":
    main()
