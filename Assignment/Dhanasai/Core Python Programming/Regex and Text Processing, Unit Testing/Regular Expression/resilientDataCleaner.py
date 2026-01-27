import re
def clean_data(text):
    try:
        if not isinstance(text, str):
            raise ValueError("Unreadable data")
        cleaned = re.sub(r'[^a-zA-Z0-9: ]', '', text)
        return f"Cleaned Data: {cleaned}"
    except Exception:
        return "Error: Unable to process data"
raw_input = "Na#me: A$le%x"
print(clean_data(raw_input))