import re
def extract_dates_from_text(text):
    pattern = r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b'
    return re.findall(pattern, text)
text = "I was born on 22/01/2005"
date = extract_dates_from_text(text)
print(date)

# venv and iterator