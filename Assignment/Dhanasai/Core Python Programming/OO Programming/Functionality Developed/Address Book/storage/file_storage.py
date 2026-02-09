def save_to_file(address_book, filename):
    with open(filename, "w") as f:
        for contact in address_book.contacts:
            f.write(str(contact) + "\n")

def read_from_file(filename):
    with open(filename, "r") as f:
        return f.readlines()
