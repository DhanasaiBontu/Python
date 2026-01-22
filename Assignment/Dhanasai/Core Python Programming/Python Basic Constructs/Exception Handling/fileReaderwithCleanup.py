def read_config(filename):
	try:
		with open(filename,'r') as file:
			print(file.read())
	except FileNotFoundError:
		print("Not found")
	finally:
		print("Check done")
read_config("missing.txt")
read_config("fileReaderwithCleanup.txt")