numbers = [1, 2, 3]
print(hasattr(numbers, "__next__"))        
it = iter(numbers)
print(hasattr(it, "__next__"))             