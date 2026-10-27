# 1.a.
inventory = {"bolts": 25, "nuts": 40, "washers": 15}
print("nuts" in inventory)
print(len(inventory))
print(15 in inventory)
print(15 in inventory.values())

# 1.b.
user_item = input("Enter an item to purchase: ")
user_qty = int(input(f"Enter a quantity of {user_item} to purchase: "))
if user_item in inventory:
    if user_qty <= inventory[user_item]:
        inventory[user_item] -= user_qty
    else:
        print(f"Insufficient stock, purchase <= {inventory[user_item]}")
else:
    print("That item is not in the inventory")
print(inventory)

# 2
sales = {"Store A": [120, 150, 90, 180, 110], "Store B": [200, 175, 160, 190, 210], "Store C": [80, 95, 120, 105, 100]}
# 2.a.
print(sales["Store A"][2])
# 2.b.
sales["Store C"].append(140)
# 2.c.
for store in sales:
    total_store_sales = sum(sales[store])
    print(f"{store} total sales: ${total_store_sales}")
# 2.d.
highest_sales = 0
highest_sales_store = ""
for store in sales:
    total_store_sales = sum(sales[store])
    if total_store_sales > highest_sales:
        highest_sales = total_store_sales
        highest_sales_store = store

print(f"{highest_sales_store} has the highest total sales: ${highest_sales}")