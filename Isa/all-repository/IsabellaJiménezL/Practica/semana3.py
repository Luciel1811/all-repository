def update_price_only(inventory):
    name = input("Enter the name of the comic to update the price -> ").strip().title()
    if name not in inventory:
        print(f"{name} is not in the inventory.")
        return

    _, current_quantity = inventory[name]["price"], inventory[name]["quantity"]

    try:
        new_price = float(input("Enter the new price -> $"))
        if new_price <= 0:
            print("Price must be a positive number.")
            return
        inventory[name] = {
            "price": new_price,
            "quantity": current_quantity
        }
        print(f"The price for {name} was successfully updated.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")