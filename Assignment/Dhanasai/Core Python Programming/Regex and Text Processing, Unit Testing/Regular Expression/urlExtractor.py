import re
def extract_urls(text):
    pattern = r'https?://\S+'
    return re.findall(pattern, text)
paragraph = "Visit https://google.com and http://github.com"
print(extract_urls(paragraph))