#va a pedir que ingreses la cotraseña hasta que ingreses la correcta 
password = "12345"
contraseña = input("Ingrese la contraseña: ")
while contraseña != password:
    contraseña = input("Ingrese la contraseña: ")
    print("")
    if contraseña == password:
        print("Bienvenido")
        break
    