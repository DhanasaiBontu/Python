import re
def extract_html_tags(text):
    pattern = r'<\s*([a-zA-Z][a-zA-Z0-9]*)\b'
    return re.findall(pattern, text)
html = "<div><a href='#'>Link</a></div>"
print(extract_html_tags(html))