import json
json_string = '{"product": "Laptop", "price": 899.99, "in_stock": true}'
py_dict = json.loads(json_string)
print(py_dict["price"])