from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))
    my_book.add_contact(Contact("Alice", "Smith", "456 Avenue", "Boston", "MA", "90001", "9876543210", "alice@example.com"))

    results = my_book.search_by_city_or_state("New York")
    print("Search results for New York:")
    for c in results:
        print(c)

if __name__ == "__main__":
    main()
