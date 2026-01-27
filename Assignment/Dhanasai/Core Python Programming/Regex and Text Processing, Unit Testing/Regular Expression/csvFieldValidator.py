import re
def validate_emails(file_path):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    try:
        with open('csvFieldValidator.csv', 'r') as file:
            for line in file:
                email = line.strip()
                if re.match(email_pattern, email):
                    print(f"Valid: {email}")
                else:
                    print(f"Invalid: {email}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")
validate_emails("emails.csv")