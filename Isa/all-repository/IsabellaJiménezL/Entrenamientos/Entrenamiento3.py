
from utils_3 import * 
# Cree un inventario pues una tienda de comics no puede estar 100% vacia 
mangas_products = [
    {"Naruto":(69900,6)},  
    {"The promised neverland":( 46900, 9 )},
    {"Akatsuki no yona":(82900, 10)},
    {"Love is war":(42900, 1)},
    {"Berserk":(37900, 2)},
    {"Batman:The killing joke":(169000, 11)},
    {"Superman vs Flash":(67900, 27)},
    {"Spider-man":(60000, 13)},
    {"Doctor Strange":(54900, 24)},
]

# Almacena y actualiza tanto el contenido del inventario como el ingresado por el usuario
inventory ={}
for manga in mangas_products:
    inventory.update(manga)

# Muestra el menú y en consecuencia todas las funciones
show_menu(inventory)




