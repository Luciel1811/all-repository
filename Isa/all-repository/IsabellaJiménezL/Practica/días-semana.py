# Según el número ingresado determina el día de la semana
numero = int(input("Ingrese un número entero entre el 1 y el 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Lunes")
elif numero == 3:
    print("Martes")
elif numero == 4:
    print("Miercoles")
elif numero == 5:
    print("Jueves")
elif numero == 6:
    print("Viernes")
elif numero == 7:
    print("Sabado")
else:
    print("Día invalido")

