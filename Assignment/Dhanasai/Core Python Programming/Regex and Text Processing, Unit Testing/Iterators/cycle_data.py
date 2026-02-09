class CycleData:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list cannot be empty")
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        value = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return value
    def reset(self):
        self.index = 0
cycler = CycleData(["A", "B", "C"])
for _ in range(7):
    print(next(cycler))
cycler.reset()
print("After reset:")
for _ in range(3):
    print(next(cycler))