from model.contact import Contact

def main():
    contact = Contact("John", "Doe", "123 Street", "New York", "NY", "10001", "1234567890", "john@example.com")
    print("Contact created:")
    print(contact)

if __name__ == "__main__":
    main()
