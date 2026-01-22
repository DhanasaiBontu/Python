import time
def measure_time(func):
	start=time.time()
	func()
	end=time.time()
	duration=(end-start)*1000
	print(f"Execution time: {duration} milliseconds")
measure_time(lambda: sum(range(100000)))