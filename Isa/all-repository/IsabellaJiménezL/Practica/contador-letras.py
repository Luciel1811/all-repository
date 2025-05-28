# Cuenta cuantas letras 'a' hay en la palabra ingresada
palabra = input ("Ingrese una palabra: ")
contador = 0

palabra = [letra.lower() for letra in palabra]
print(palabra.count('a')) 