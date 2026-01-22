n= int(input("Enter number of config dictionaries:"))
merged_config={}
for i in range(n):
	config_input=input(f"Enter dictionary {i+1}:")
	config_dict=eval(config_input)
	merged_config.update(config_dict)
print("Merged configuration:",merged_config)