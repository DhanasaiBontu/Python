def palindrome_check(text):
    cleaned = ""
    for c in text:
        if c.isalnum():
            cleaned +=c.lower()
    return cleaned == cleaned[::-1]
text = "A man, a plan, a canal: Panama"
print(palindrome_check(text))