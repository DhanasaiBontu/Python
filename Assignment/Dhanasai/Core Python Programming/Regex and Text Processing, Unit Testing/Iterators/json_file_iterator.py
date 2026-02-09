import json
class JSONFileIterator:
    def __init__(self, file_path):
        self.file = open(file_path, "r", encoding="utf-8")
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            line = line.strip()
            if not line:
                continue
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
iterator = JSONFileIterator("json_file_iterator.json")

for record in iterator:
    print(record)