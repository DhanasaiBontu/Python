import json
def update_inventory(product_name, quantity):
    with open("inventoryUpdateSystem.json","r") as file:
        inventory = json.load(file)
    inventory[product_name] = quantity
    with open("inventoryUpdateSystem.json","w") as file:
        json.dump(inventory,file,indent = 4)
    print(inventory)
update_inventory("Laptop", 15)