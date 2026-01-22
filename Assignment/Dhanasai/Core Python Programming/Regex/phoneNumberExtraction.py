import re
def extract_phone_number(text):
    pattern = r'\b\d{10}\b'
    return re.findall(pattern, text)
text = "I changed my phon enumber. Now it is 9876543210"
print(extract_phone_number(text))