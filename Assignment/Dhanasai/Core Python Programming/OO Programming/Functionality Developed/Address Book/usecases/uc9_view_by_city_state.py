from model.contact import Contact
from model.address_book import AddressBook

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))
    my_book.add_contact(Contact("Alice", "Smith", "456 Avenue", "New York", "NY", "90001", "9876543210", "alice@example.com"))
    
    city = "New York"
    persons_in_city = my_book.search_by_city_or_state(city)
    
    print(f"Persons in {city}:")
    for c in persons_in_city:
        print(c)

if __name__ == "__main__":
    main()
