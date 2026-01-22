import os
def scan_directory(path):
	files=[]
	for itam in os.listdir(path):
		full_path=os.path.join(path,item)
	if os.path.isfile(full_path):
		files.append(full_path)
	elif os.path.isdir(full_path):
		files.extend(scan_directory(full_path))
	return files