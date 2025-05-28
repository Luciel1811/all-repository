numero = int(input("Ingrese un número -> "))
suma = 0

for i in range(1, numero):
    if i %2 != 0 and i %3 !=0:
        suma += i
        print(i)
        
    
print(f"La suma de los número es: {suma}")
        
