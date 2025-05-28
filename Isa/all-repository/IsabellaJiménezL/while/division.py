numero1 = int(input("\nIngrese el primer número -> "))
while True:
    try:
        numero2 = int(input("\nIngrese el segundo número -> "))
        if numero2 == 0:
            raise ValueError()
        break
    except ValueError:
        print("\nEl número no puede ser 0")
    
division = numero1/numero2

print(f"el resultado de la division es {division}")

