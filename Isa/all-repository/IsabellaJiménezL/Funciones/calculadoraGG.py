def calculadora(a:int,b:int, operacion:str):
    if operacion == "suma":
        return a+b
    elif operacion == "resta":
        return a-b
    elif operacion == "multiplicacion":
        return a*b
    elif operacion == "division":
        if b != 0:
            return a/b
        else:
            return "No se puede dividir entre 0"
    else:
        return "Operacion invalida"

operacion = ""

while operacion != "salir":
    print("""\n---Calculadora---
    operaciones disponibles: suma, resta, multiplicación y división
    Escribe 'salir' para terminar. \n """)
    
    operacion = input("¿Que operación desea realizar? -> ").lower()
    
    if operacion == "salir":
        print("Gracias por usar la calculadora")
        break
    try:
        number_1 = int(input("Ingrese el primer numero -> "))
        number_2 = int(input("Ingrese el segundo numero -> "))
    except ValueError:
        print("Ingrese valores numericos validos")
        continue
    
    resultado = calculadora(number_1,number_2,operacion)
    print(f"El resultado es: {resultado}")