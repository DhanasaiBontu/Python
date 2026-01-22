from collections import Counter
text = "great service great product"
n=2
words=text.split()
word_counts=Counter(words)
top_n=word_counts.most_common(n)
print(top_n)