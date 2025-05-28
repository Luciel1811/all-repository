# Crea un programa que muestre todos los múltiplos de 3 entre 1 y 30.
#     • Resolver primero con while.
#     • Resolver luego con for con range().

# Se crea la lista de números 
i = 1
numbers = []
while i < 31:
    numbers.append(i)
    i += 1
# print(numbers)

# Recorre la lista y si encuentra un multiplo de 3 lo imprime
for value in numbers:
    if value %3 == 0:
        print(value)