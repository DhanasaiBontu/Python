import json

contact = {
    "name": "Alex", 
    "phone": "123-456-7890", 
    "email": "alex@example.com"
    }

y = json.dumps(contact)
print(y)