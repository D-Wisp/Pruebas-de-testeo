class NodoArbol:
    def __init__(self, dato):
        '''Clase Nodo para implementacion de arboles en py'''
        self.informacion = dato
        self.izquierda = None
        self.derecha = None
        

def arbol_vacio(raiz) -> bool:
    return(raiz is None)

def insertar_nodo(raiz, dato):
    '''
    Funcion que inserta nodos en el arbol
    Si son menores al valor del nodo comparado, a la IZQUIERDA
    Si son mayores al nodo comparado, a la DERECHA
    '''
    if arbol_vacio(raiz):
        raiz = NodoArbol(dato)
    elif (raiz.informacion <= dato):
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    else:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    return raiz

def imprimir_arbol(raiz):
    if arbol_vacio(raiz):
        print(" - ")
    else:
        print(f"[ {raiz.informacion} ]")
        print(f"Rama inzquierda del nodo {raiz.informacion}")
        imprimir_arbol(raiz.izquierda)
        print(f"Rama derecha del nodo {raiz.informacion}")
        imprimir_arbol(raiz.derecha)
        
        
arbol = insertar_nodo(None, 32)
arbol = insertar_nodo(arbol, 11)
arbol = insertar_nodo(arbol, 44)
arbol = insertar_nodo(arbol, 5)
imprimir_arbol(arbol)