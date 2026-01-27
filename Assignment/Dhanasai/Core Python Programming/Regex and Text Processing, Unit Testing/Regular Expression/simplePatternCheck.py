import re
def starts_with_capital(text):
    if re.match(r'^[A-Z]', text):
        return "Starts with a capital letter."
    else:
        return "Does not start with a capital letter."
print(starts_with_capital("Python"))
print(starts_with_capital("python"))