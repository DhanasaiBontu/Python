def smart_calculate(a_str, b_str):
	try:
		a = int(a_str)
		b = int(b_str)
		return a/b
	except ValueError:
		print("Invalid Number")
	except ZeroDivisionError:
		print("Cannot divide by zero")
smart_calculate("10","0")
smart_calculate("Ten","0")