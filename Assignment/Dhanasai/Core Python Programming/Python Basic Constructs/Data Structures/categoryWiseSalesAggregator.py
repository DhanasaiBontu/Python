sales_data = [("Electronics",1000),("Furniture",2000),("Electronics",1500)]
category_totals={}
for category,amount in sales_data:
	if category in category_totals:
		category_totals[category]+=amount
	else:
		category_totals[category]=amount
print(category_totals)