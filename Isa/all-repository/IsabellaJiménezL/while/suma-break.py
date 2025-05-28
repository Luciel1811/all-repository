#suma los numeros y sigue pidiendo hasta que se ingrese un 0
suma = 0

while True:
    numero = int(input("Ingrese un número -> "))
    if numero == 0:
        break
    suma+=numero
    
print (suma)
