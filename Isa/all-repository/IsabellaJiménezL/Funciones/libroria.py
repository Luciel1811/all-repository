#Registro de Libros Prestados
#Simula un sistema donde el usuario registre libros prestados por una biblioteca. Por cada
#libro debe ingresar título, autor y número de días prestado. Si pasa de 7 días, se cobramulta por día adicional. Muestra resumen final de libros prestados, con costo total si hay
#multas. Usa listas, funciones, bucles y condicionales

print("Bienvenido a ✨La libroria✨")

def creation_dictionary_list():
    amount = int(input("¿Cuantos libros deseas retornar? -> "))

    dictionary_list = []
    penalty_per_day = 2
    limit_days = 7
    for i in range(amount):
        dictionary = {}
        
        dictionary["Title"] = input(f"\n¿Cual es el titulo del libro {i+1}? -> ")
        dictionary["Author"] = input(f"\n¿Quien es el autor del libro {i+1}? -> ")
        days = int(input(f"\n¿Cuantos días alquilaste el libro {i+1}? -> "))
        dictionary["days"] = days

        if days > limit_days:
            extra_days = days - limit_days
            penalty = extra_days*penalty_per_day
            dictionary["penalty"] = penalty
        else:
            dictionary["penalty"] = 0

        dictionary_list.append(dictionary)

    return dictionary_list

book_list = creation_dictionary_list()

print("\nLa lista de libros con toda la información es:")
for book in book_list:
    print(book)
