palabra = input("Ingrese una palabra -> ")
suma = 0

for letra in palabra:
    if letra == "a":
        suma+=1
        
print(f"La letra A aparece {suma}{' vez' if suma==1 else ' veces'} en la palabra {palabra}")        