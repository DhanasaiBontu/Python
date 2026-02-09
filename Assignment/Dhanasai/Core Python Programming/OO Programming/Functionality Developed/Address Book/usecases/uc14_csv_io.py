import csv
from model.contact import Contact
from model.address_book import AddressBook

def save_to_csv(address_book, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["FirstName","LastName","Address","City","State","Zip","Phone","Email"])
        for c in address_book.contacts:
            writer.writerow([c.first_name,c.last_name,c.address,c.city,c.state,c.zip_code,c.phone_number,c.email])

def main():
    my_book = AddressBook("Friends")
    my_book.add_contact(Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com"))

    save_to_csv(my_book, "address_book.csv")
    print("Saved to address_book.csv")

if __name__ == "__main__":
    main()
