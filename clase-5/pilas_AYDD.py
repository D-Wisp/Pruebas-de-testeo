class Nodo:
    '''clase que representa un nodo para construir una pila'''
    def __init__(self, dato=None , siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

        
class Pila:
    '''implementacion de una pila en py'''
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def push(pila, dato_nuevo): # metodo para apilar un nuevo elemento
    '''agrega un nuevo nodo a la cima de la pila'''
    nodo_a_apilar = Nodo(dato_nuevo)
    nodo_a_apilar.siguiente = pila.cima
    pila.cima = nodo_a_apilar
    pila.tamanio += 1
    
    
def pop(pila): # desapila un elemento de la cima de la pila
    '''devuelve el ultimo nodo ingresado LIFO, y lo remueve de la pila'''
    if pila.tamanio == 0:
        raise RuntimeError("No hay mas elementos para remover")
    else:
        nodo_a_retornar = pila.cima
        pila.cima = nodo_a_retornar.siguiente
        pila.tamanio -= 1
        return nodo_a_retornar       
        
def is_empty(pila):
    return (pila.tamanio == 0)

def top(pila):
    '''muestra el valor del nodo en la cima de la pila'''
    if pila.tamanio == 0:
        return None
    else:
        return pila.cima.dato
  
def print_pila(pila):
    if pila.tamanio == 0:
        print("PILA VACIA!!")
    else:
        nodo = pila.cima
        print(pila.cima.dato)
        while(nodo.siguiente is not None):
            nodo = nodo.siguiente
            print(pila.cima.dato)

            
pila1 = Pila()
push(pila1, 'A')
push(pila1, 'B')
push(pila1, 'C')
print(f"el ultimo elemeto apilado es: {top(pila1)}")
print(pila1.tamanio)
print(f"La pila esta vacia? {is_empty(pila1)}")

print("--------")
print_pila(pila1)
print("--------")

resultado = pop(pila1)
print(resultado.dato)
resultado = pop(pila1)
print(resultado.dato)
resultado = pop(pila1)
print(resultado.dato)
print(f"el ultimo elemeto apilado es: {top(pila1)}")
print(f"La pila esta vacia? {is_empty(pila1)}")
print_pila(pila1)
resultado = pop(pila1)
print(resultado.dato)
print(pop(pila1))
print(pila1.cima.dato)
print(pila1.tamanio)
