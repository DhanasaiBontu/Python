from model.contact import Contact

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact: Contact):
        if contact in self.contacts:
            print(f"Duplicate contact: {contact.first_name} {contact.last_name}")
        else:
            self.contacts.append(contact)

    def edit_contact(self, first_name, last_name, **kwargs):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                for key, value in kwargs.items():
                    if hasattr(contact, key):
                        setattr(contact, key, value)
                break

    def delete_contact(self, first_name, last_name):
        self.contacts = [c for c in self.contacts if not (c.first_name.lower() == first_name.lower() and c.last_name.lower() == last_name.lower())]

    def search_by_city_or_state(self, location):
        return [c for c in self.contacts if c.city.lower() == location.lower() or c.state.lower() == location.lower()]

    def sort_by_attribute(self, attribute):
        self.contacts.sort(key=lambda c: getattr(c, attribute))

    def count_by_city_or_state(self, location):
        return len(self.search_by_city_or_state(location))
