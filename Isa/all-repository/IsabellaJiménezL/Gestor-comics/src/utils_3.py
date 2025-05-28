# Añade productos al inventario y solo almacena los que se ingresan correctamente
def add_product(inventory):
    name = input("\nIngrese el nombre del comic a agregar -> ").strip().capitalize()
    if name in inventory:
        print(f"🧐El comic {name.title()} ya se encuentra en el inventario.🧐")
        return
    try:
        price = float(input("💲Ingrese el precio del comic -> $"))
        amount = int(input("Actualice la cantidad de comics que llegaron a la tienda -> "))
        if price <= 0 or amount <= 0:
            print("\n❌El valor y la cantidad deben ser valores positivos.❌")
            return
        inventory[name] = (price,amount)
        print(f"\n✅ El comic {name.title()} fue agregado correctamente. ✅")
    except ValueError:
        print("\n❌Ha ingresado un dato invalido, recuerde que debe ser númerico y positivo.❌")


# Consulta si el comic se encuentra en el inventario
def consult_product(inventory):
    name = input("\nIngrese el nombre del comic que desea consultar -> ").strip().capitalize()
    if name in inventory:
        price, amount = inventory[name]
        print(f"\nDetalles del comic {name.title()}: ")
        print(f"Precio ${price:,.0f}")
        print(f"Hay {amount} unidades disponibles")
    else:
        print(f"🧐El comic {name.title()} no se encuentra en el inventario.🧐")


# Actualiza el precio y las unidades disponibles del comic seleccionado
def update_product(inventory):
    name = input("\nIngrese el nombre del comic que desea actualizar -> " ).capitalize()
    if name in inventory:
        try:
            new_price = float(input(f"💲Ingrese el nuevo precio del comic {name.title()} -> $"))
            new_amount = int(input(f"Actualice la cantidad de comics que llegaron a la tienda -> "))
            if new_price <= 0 or new_amount <= 0:
                print("\n❌El valor y la cantidad deben ser valores positivos.❌")
            return
            inventory[name] = (new_price,new_amount)
        except ValueError:
            print("\n❌Error: debe ingresar números positivos❌")
    else:
        print (f"\n🧐El comic {name.title()} no se encuentra en el inventario.🧐")


# Elimina del inventario al comic seleccionado
def anihilate_product(inventory):
    name = input("\nIngrese el nombre del comic que desea eliminar -> ").capitalize()
    if name in inventory:
        del inventory[name]
        print(f"\n✅ El comic {name.title()} se elimino correctamente ✅")
    else:
        print(f"\n🧐El comic {name.title()} no se encuentra en el inventario.🧐")


# Calcula el valor total de todos los comics en la tienda
def total_value(inventory):
    stock = map(lambda x: x[0]* x[1], inventory.values())
    total = sum(stock)
    print(f"\nEl valor total del inventario es -> 💲{total:,.2f}")


# Muestra el inventario de manera bonita
def show_inventory(inventory):
    print("\n📦 Inventario actual:\n")
    print(f"{'Nombre':<25} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 45)
    for name, (price, amount) in inventory.items():
        print(f"{name:<25} ${price:<10,.0f} {amount:<10}")

# Muestra el menú de opciones
def show_menu (inventory):
    validation = True
    while validation == True:
        print("\nBienvenido querido trabajador al gestor de inventario de ✨Isamics✨ la tienda de comics estrella.")
        print("\nA continuación vera un menú con las opciones disponibles para optimizar su trabajo.")
        print("\n---✅ Labores a realizar ✅---")
        print("\n1. Agregar producto al inventario")
        print("\n2. Consultar existencia de producto en el inventario")
        print("\n3. Actualizar producto del inventario")
        print("\n4. Eliminar producto del inventario")
        print("\n5. Calcular total del inventario")
        print("\n6. Ver el inventario")
        print("\n7. Salir.")

        option = input("\nIngrese el número correspondiente a la acción deseada -> ")
        if option == "1":
            add_product(inventory)
        elif option == "2":
            consult_product(inventory)
        elif option == "3":
            update_product(inventory)
        elif option == "4":
            anihilate_product(inventory)
        elif option == "5":
            total_value(inventory)
        elif option == "6":
            show_inventory(inventory)
        elif option == "7":
            print("\n✨Gracias por usar el gestor de inventario para su tienda de comics de confianza✨ \n")
            validation = False
        else:
            print("\n❌Selección invalida, por favor ingrese uno de los números mostrados en el menú.❌")