#Función que saluda
def greetings():
    print("Hola ¿como estas?")

greetings()

#Crear una función que reciba el nombre del usuario y salude.
def saludo(nombre):
    print(f"hola mi nombre es {nombre}")
    
nombre = input("Ingrese su nombre: ")
saludo(nombre)
saludo("Mirta")

#Función que pide el nombre y la edad al usuario
def identification(name:str, age:int):
    print(f"Hello my name is {name} and i'm {age} years old")

user_name = input("Write your name here -> ")
user_age = input("Write your age here -> ")
identification(user_name,user_age)