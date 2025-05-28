inventory = {}

# Agregar productos
def add_product(inventory):
    try:
        products = int(input("\nEnter the number of brands you want to add (Must be more than 5) -> "))
        if products < 5:
            print("You must add at least 5 products.")
            return

        for i in range(products):
            name_product = input("\nEnter the brand's name -> ").strip().capitalize()
            try:
                price = float(input(f"Enter the {name_product}'s price per unit -> $"))
                if price <= 0:
                    print("\nInvalid price. It must be greater than 0.")
                    continue

                amount = int(input(f"Enter the number of {name_product} shoes that arrived -> "))
                if amount <= 0:
                    print("Invalid amount. It must be greater than 0.")
                    continue

                inventory[name_product] = (price, amount)

            except ValueError:
                print("Invalid value. Please enter valid numbers.")
    except ValueError:
        print("Invalid value. Please enter a valid number.")

# Buscar producto
def search_product(inventory):
    name = input("\nEnter the name of the shoe brand you're looking for -> ").strip().capitalize()
    if name in inventory:
        price, amount = inventory[name]
        print(f"\n{name} brand details: ")
        print(f"Price per unit: ${price:,.2f}")
        print(f"Stock: {amount} pairs")
    else:
        print(f"{name} brand is not in stock.")

# Modificar precio
def modify_price(inventory):
    name = input("Enter the brand name whose price you want to update -> ").strip().capitalize()
    if name in inventory:
        try:
            new_price = float(input(f"Enter the new price for {name} -> $"))
            if new_price <= 0:
                print("The price must be greater than 0.")
                return
            _, amount = inventory[name]
            inventory[name] = (new_price, amount)
            print(f"Price for {name} updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print(f"{name} brand is not in stock.")

# Eliminar producto
def erase_product(inventory):
    name = input("Enter the brand name to remove from inventory -> ").strip().capitalize()
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} was never in the inventory.")

# Calcular valor total del inventario
def total_value(inventory):
    total = sum(price * amount for price, amount in inventory.values())
    print(f"\nTotal inventory value: ${total:,.2f}")

# Mostrar inventario
def show_inventory(inventory):
    if not inventory:
        print("\nInventory is empty.")
        return
    print("\n📦 Updated inventory:\n")
    print(f"{'Brand':<25} {'Price':<10} {'Amount':<10}")
    print("-" * 45)
    for name, (price, amount) in inventory.items():
        print(f"{name:<25} ${price:<10,.2f} {amount:<10}")

# Menú principal
def show_menu(inventory):
    while True:
        print("\nWelcome to ✨Ishoes✨ Inventory Manager")
        print("\n---✅ Menu ✅---")
        print("1. Add products to the inventory")
        print("2. Search product")
        print("3. Update product price")
        print("4. Delete a product")
        print("5. Calculate total inventory value")
        print("6. Show inventory")
        print("7. Exit")

        option = input("\nEnter your option -> ")
        if option == "1":
            add_product(inventory)
        elif option == "2":
            search_product(inventory)
        elif option == "3":
            modify_price(inventory)
        elif option == "4":
            erase_product(inventory)
        elif option == "5":
            total_value(inventory)
        elif option == "6":
            show_inventory(inventory)
        elif option == "7":
            print("\nThanks for using the inventory manager!\n")
            break
        else:
            print("❌ Invalid option. Please choose from the menu. ❌")