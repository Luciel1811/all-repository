#pregunta que ingreses un número hasta que lo adivines
secreto = 7
numero = int(input("Adivine el número -> "))
while numero != secreto:
    numero = int(input("Adivine el número -> "))
    if numero == secreto:
        print("Felicitaciones, haz adivinado el número")
        break
