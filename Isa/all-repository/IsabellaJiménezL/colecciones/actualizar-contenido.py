#Creación del diccionario
coder = {
    "nombre": "Isabella",
    "apellido": "Jiménez",
    "edad": 20,
    "estatura": 169,
    "peso": 64
}
print(coder)

#Actualizacion de datos
coder["genero"] = "femenino"
coder["estado"] = "viva"
coder["ciudad"] = "Barranquilla"

print(coder)

#Eliminar un valor
del(coder["estado"])
print(coder)