def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except (TypeError, ValueError):
        return "Error: Invalid input type."
print(safe_divide(10, 'a'))
print(safe_divide(10, 0))     
print(safe_divide(10, 2))