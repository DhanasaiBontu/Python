import random
data = {"name": "Dhana", "age": 20, "city": "Hyderabad"}
key, value = random.choice(list(data.items()))
print("Key:",key)
print("Value:",value)