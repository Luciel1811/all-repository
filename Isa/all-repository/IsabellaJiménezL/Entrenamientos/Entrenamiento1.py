# Pedir el nombre del producto
# Pedir el precio del producto por unidad
# Pedir la cantidad de productos a comprar
# Porcentaje de descuento

# Se pide el nombre del producto
print("\nIngrese el nombre del producto que desea comprar: ")
producto = input()

# Se ingresa el precio del producto y valida que el valor ingresado sea numérico
while True:
    try:
        print("\nIngrese el valor del producto: ")
        precio = float(input("$"))
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        break
    except ValueError:
        print("⚠️ Ingrese un valor numérico valido ⚠️")

# Se ingresa la cantidad de productos a comprar y valida que el dato ingresado sea numérico
while True:
    try:
        print("\nIngrese la cantidad que va a comprar: ")
        cantidad = int(input())
        if cantidad < 1:
            raise ValueError("Debe comprar al menos un productos")
        break
    except ValueError:
        print("⚠️ Ingrese un número entero valido ⚠️")

CostoTotal = cantidad*precio

# Se ingresa el porcentaje de descuento y valida que el dato ingresado sea numérico y este entre el rango establecido
while True:
    try:
        print("\nIngrese el porcentaje de descuento(si no aplica ingrese 0)")
        porcentaje = int(input())
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError(" El porcentaje debe estar entre 0 y 100 ")
        break
    except ValueError:
        print("⚠️ Ingrese un número entre 0 y 100 ⚠️")

# Se asigna el descuento
if porcentaje > 0:
    descuento = (porcentaje / 100) * CostoTotal
    CostoTotal -= descuento
else:
    descuento = 0
    print("No se aplico ningun descuento.")

# Se imprimen los datos para mostrarlos al usuario
print(f"""
         El resumen de su compra es:

       Nombre del producto ->   {producto}
       Valor del producto  ->   ${precio:.2f}
       Cantidad comprada   ->   {cantidad}
       Subtotal            ->   ${cantidad*precio:.2f}
       Descuento aplicado  ->   {porcentaje}%
       Monto descontado    ->   ${descuento:.2f}
       Total a pagar       ->   ${CostoTotal:.2f}

       """)