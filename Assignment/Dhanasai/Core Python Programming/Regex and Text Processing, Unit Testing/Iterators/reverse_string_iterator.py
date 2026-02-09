class ReverseStringIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1   
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1          
            return char
        else:
            raise StopIteration
r = ReverseStringIterator("Python")
for ch in r:
    print(ch)