def case_normalizer(text):
    return ' '.join(text.lower().split())
text = " hello    world   q"
print(case_normalizer(text))