def calculate_net_salary(gross, tax_rate):
	tax = gross*(tax_rate/100)
	net_salary=gross-tax
	return net_salary
print(calculate_net_salary(50000,10))