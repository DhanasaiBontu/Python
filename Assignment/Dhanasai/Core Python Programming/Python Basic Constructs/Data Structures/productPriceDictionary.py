products = input("Enetr product names: ").split()
prices = list(map(int, input("Enter product prices:").split()))
product_price = dict(zip(products,prices))
print(product_price)