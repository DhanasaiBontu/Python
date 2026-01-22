number = int(input("Enter an integer:"))
bin_value = bin(number)[2:]
print(bin_value.zfill(8))
print(bin_value.zfill(10))