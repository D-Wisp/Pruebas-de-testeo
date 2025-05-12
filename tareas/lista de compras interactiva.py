lista_de_compras = []

def agregar_producto():
    producto = input("ingresa el producto: ")
    cantidad = input("cantidad: ")
    precio = input("precio: ")
    lista_de_compras.append((producto, cantidad, precio))
    print(f"el producto {producto} ha sido agregado a la lista de compras.")
    
def lista_productos():
    print("\nlista de compras")
    for producto, cantidad, precio in lista_de_compras:
        print(f"producto: {producto}, cantidad: {cantidad}, precio: {precio}")  
        
def eliminar_producto():
    producto = input("ingresa el producto que quieras eliminar de la lista: ")
    for i, (p, c, pr) in enumerate(lista_de_compras):
        if p == producto:
            del lista_de_compras[i]
            print(f"el producto {producto} ha sido eliminado de la lista")
                      

while True:
    print("\n1. agregar producto")
    print("2. ver lista de productos")
    print("3. eliminar producto")
    print("4. salir")
    apciones = input("ingresa una opcion: ")
    
    if apciones == "1":
        agregar_producto()
    elif apciones == "2":
        lista_productos()
    elif apciones == "3":
        eliminar_producto()
    elif apciones == "4":
        break
    else:
        print("opcion no valida, intenta de nuevo.")