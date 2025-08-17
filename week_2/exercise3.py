# # Python program to sum up all the items in a dictionary

# fruits=dict()
# fruits={'mango':10,'oranges':50,'banana':30}

# total =sum(fruits.values())
# print(total)

#dictionary to store product information (name, price, quantity)
product_info={}

print ("\n options: additem | updateitem | removeitem | show | exit  ")
choice = input("Enter a task: ").lower()

while True :
    if choice=='additem':
        name=input('enter product name:')
        price=float('enter price:')
        quantity=float('provide quantity: ')
        product_info[name]={'price':price,'quantity':quantity}
        print('{name} added successfully')
        
    elif choice == "updateitem":
        name = input("Enter product name to update: ")
        if name in product_info:
            price = input("Enter new price (leave blank to keep current): ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            if price:
                product_info[name]["price"] = float(price)
            if quantity:
                product_info[name]["quantity"] = int(quantity)
            print(f"{name} updated successfully!")
        else:
            print("Product not found.")
            break




