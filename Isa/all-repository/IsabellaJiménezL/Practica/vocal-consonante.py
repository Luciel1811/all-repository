# Determina si el caracter ingresado es vocal o consonante
vocales = ["a", "e", "i", "o", "u"]

consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
"n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

user_letter = input('Introduce una letra ').lower()

if len(user_letter) == 1: # isdigit, 
    if user_letter in vocales:
        print('Es una vocal')
    elif user_letter in consonantes:
        print('No es una vocal') 
    elif not user_letter.isalpha(): 
        print('Carácter no valido')
    else:
        print('Debe ingresar un solo carácter')
