# Pedir la primera nota
# Evaluar que la nota sea adecuada
# Crear una lista de notas ingresadas por el usuario
# Evaluar que notas aprobo y cuales no
# Calcular el promedio de las notas (for)
# Contar cuantas notas son mayores que la primera ingresada(while)
# Buscar una calificación y cuantas veces aparece

#Lo primero es evaluar si la nota ingresada por el usuario esta aprobada o reprobada
print("\n1️⃣ A continuación evaluaremos una nota, el rango es de 1 a 100, recuerde que con 60 se aprueba ")
while True:    
    try:
        first_note = float(input("\nIngrese su primera nota a ser evaluada -> "))
        if first_note < 60 and first_note > 0:
            print("\n🥲 Lo sentimos, usted a reprobrado 🥲")
            break
        elif first_note >= 60 and first_note <75:
            print("🤓 Has aprobado, sin embargo aun puedes mejorar,sigue esforzándote 🤓")
        elif first_note >=75 and first_note <90:
            print("\n🥳Felicitaciones, su nota ha sido muy buena y ha aprobado🥳")
            break
        elif first_note >= 90 and first_note <= 100:
            print("\n ✨Felicitaciones, su nota ha sido excelente y ha aprobado✨")
            break
        else:
            print("\n❗Nota invalida, por favor ingrese una nota dentro del rango especificado❗")
    except ValueError:
        print("\n🤔Por favor ingrese un valor numerico adecuado🤔")

#Aqui se crea una lista vacia para ir almacenando las notas ingresadas por el usuario
print("\n2️⃣ A continuación vamos a evaluar una cantidad de notas separadas por coma(,)")

notes_list = []
i = 0
total_notes = 0
while True:    
    notes = input("\n Ingrese las calificaciones deseadas y no olvide separarlas por comas (,) -> ")
    if " " in notes_list:
        print("\n🤔Ingrese solo las notas separadas por una coma(,)🤔")

    try:
        notes_list = [float(note.strip()) for note in notes.split(",")]#Quita los espacios en blanco y separa los valores con comas 
#Valida que el rango sea el adecuado
        notes_status = True
        for note in notes_list:
            if note < 0 or note > 100:
                print("\n ❗ Ha ingresado un valor incorrecto, recuerde que el rango es de 1 a 100 ❗")
                notes_status = False
                break       
#Saca el promedio
            if notes_status:
                total = 0
                for note in notes_list:
                    total += note
                average = total/len(notes_list)
        break
    except ValueError:
        print("\n❗ Ha ingresado un valor incorrecto, recuerde que debe ser numerico ❗")
#Se ingresa una nueva nota y busca cuales de la lista son mayores  
print("\n3️⃣ A continuación vamos a evaluar las notas ingresadas anteriormente con base en una nueva nota ")

while True:
    try:
        compare_values= float(input("\nIngrese una nota para compararla con las ingresadas anteriormente -> "))
        if compare_values < 0 or compare_values > 100:
            print("\n❗La nota debe estar entre 0 y 100❗")
        else:
            break
    except ValueError:
        print("\n❗Ha ingresado un valor incorrecto, recuerde que debe ser numerico❗")
    
count = 0
for note in notes_list:
    if note > compare_values:
        count += 1
#Se ingresa una nueva nota y evalua cuantas veces aparece ese mismo valor en la lista de notas
print("\n4️⃣ A continuación vamos a evaluar cuantas veces aparece una nota ")


quantity = float(input("\nIngrese el valor que desea encontrar en la lista de notas -> "))
equal = 0

for i in range (len(notes_list)):
    if notes_list[i] == quantity:
        equal += 1
        
#Imprime los resultados
print("")
print("-------------------------------------------------------------------------------------------")
print(f"Las notas ingresadas son                  -> {notes_list}")
print(f"El promedio de las notas es               -> {average}")
print(f"La nota ingresada para comparar es        -> {compare_values}")
print(f"La cantidad de notas mayor a {compare_values} son     -> {count} ")
print(f"La calificación a buscar es               -> {quantity}")
print(f"La cantidad de veces que {quantity} aparece son -> {equal}")