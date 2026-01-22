def get_age(input_str):
	try:
		return int(input_str)
	except ValueError:
		return -1
print(get_age("twenty"))
print(get_age("20"))