import re
def validate_form(name, email, phone):
    try:
        if not name or not email or not phone:
            raise ValueError("Missing input field.")
        name_pattern = r'^[A-Za-z ]+$'
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        phone_pattern = r'^\d{10}$'
        if not re.match(name_pattern, name):
            raise ValueError("Invalid name format.")
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format.")
        if not re.match(phone_pattern, phone):
            raise ValueError("Invalid phone number format.")
        return "Valid inputs."
    except ValueError as e:
        return f"Error: {e}"
print(validate_form("Alex", "alex@corp.com", "9876543210"))