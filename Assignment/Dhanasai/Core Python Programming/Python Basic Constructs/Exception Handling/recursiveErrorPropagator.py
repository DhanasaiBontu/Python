import os
def scan_files(path, depth=0):
	if depth>3:
		return
	try:
		for item in os.listdir(path):
			full_path = os.path.join(path,item)
			if os.path.isdir(full_path):
				scan_files(full_path, depth+1)
	except RecursionError:
		print("Recursion Limit Reached")
scan_files("nonexistant",1)
