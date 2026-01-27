import re
def sentence_splitter(text):
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]
text = "Hi! How are you? I'm fine."
print(sentence_splitter(text))