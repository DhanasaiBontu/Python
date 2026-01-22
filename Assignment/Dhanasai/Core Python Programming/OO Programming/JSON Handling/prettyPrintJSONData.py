import json
def pretty_print(data):
    formatted_json = json.dumps(data,indent = 4)
    print(formatted_json)
data = {"user": {"name": "Alex", "age": 25, "city": "Mumbai"}}
pretty_print(data)