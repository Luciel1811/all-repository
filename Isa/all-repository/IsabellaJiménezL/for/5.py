# Solicita al usuario un número inicial y muestra una cuenta 
# # regresiva hasta llegar a 0 usando for con range(inicio, -1, -1).

numero = int(input("Ingrese un número -> "))

for valor in range(numero, -1, -1):
    print(valor)