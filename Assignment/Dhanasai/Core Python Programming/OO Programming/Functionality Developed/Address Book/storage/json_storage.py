import json

def save_to_json(address_book, filename):
    contacts_list = [contact.__dict__ for contact in address_book.contacts]
    with open(filename, "w") as f:
        json.dump(contacts_list, f, indent=4)

def read_from_json(filename):
    with open(filename, "r") as f:
        return json.load(f)
