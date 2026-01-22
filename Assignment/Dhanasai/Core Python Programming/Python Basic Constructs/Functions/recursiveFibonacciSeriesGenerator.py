def fibonacci(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)

def generate_fibonacci(n):
	series=[]
	for i in range(n):
		series.append(fibonacci(i))
	return series
print(generate_fibonacci(6))