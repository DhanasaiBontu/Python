class Sentence:
    def __init__(self, text):
        self.words = text.split()
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration
s = Sentence("Python makes iteration simple and powerful")
for word in s:
    print(word)
