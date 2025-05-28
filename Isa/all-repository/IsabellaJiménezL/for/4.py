vocales = ["a", "e", "i", "o", "u"]
palabra = input("Ingrese una palabra -> ")
i=0 
palabra_cambiada = ""
cambios = {
    "a":"@",
    "e":"&",
    "i":"%",
    "o":"/",
    "u":"*"
}
for letra in palabra:
    if letra in vocales:
        palabra_cambiada += cambios[letra]
        i+=1
    else:
        palabra_cambiada += letra

print(f"Palabra modificada -> {palabra_cambiada}")
print(f"Vocales reemplazadas -> {i}")