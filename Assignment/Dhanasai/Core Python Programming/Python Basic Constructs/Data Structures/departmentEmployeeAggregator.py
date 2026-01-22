from collections import defaultdict
n=input(input("Enter number of recoreds:"))
dept_employees=defaultdict(list)
for i in range(n):
	dept,emp=input("Enter department and employee name:").split()
	dept_employees[dept].append(emp)
print(dict(dept_employees))