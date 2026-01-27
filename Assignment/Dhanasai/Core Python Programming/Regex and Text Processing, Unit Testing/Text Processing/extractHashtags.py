def extract_hashtags(text):
    hashtags = []
    for word in text.split():
        if word.startswith('#'):
            hashtags.append(word)
    return hashtags
text = "Learning #Python and #DataScience today!"
print(extract_hashtags(text))