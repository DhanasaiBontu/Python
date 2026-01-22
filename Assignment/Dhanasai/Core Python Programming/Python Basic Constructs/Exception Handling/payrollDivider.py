def safe_divide_bonus(bonus, count):
	try:
		return bonus/count
	except ZeroDivisionError:
		return 0.0
print(safe_divide_bonus(1000,0))
print(safe_divide_bonus(0,1000))
print(safe_divide_bonus(10000,1000))