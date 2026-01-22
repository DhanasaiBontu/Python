def divide_sales(num, den):
	try:
		result = num/den
	except ZeroDivisionError:
		return 0
	else:
		print("Success:",result)
	finally:
		print("Log Closed")
divide_sales(100,0)
divide_sales(1000,100)