import string
def remove_punctuation(text):
    return ''.join(
        ch for ch in text
        if ch not in string.punctuation
    )
text = "Wow!!! This is great... isn't it?" 
print(remove_punctuation(text))