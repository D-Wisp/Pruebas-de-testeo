class Nodo:
    '''nodo que utilizaremos para construir colas'''
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
        
        
class Cola:
        '''implementacion de una cola en python'''
        def __init__(self):
            self.frente = None
            self.final = None
            self.tamanio = 0
            
            
def enqueue(cola, dato): # encolar / push
    nodo = Nodo(dato)
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.siguiente = nodo
    cola.final = nodo
    cola.tamanio += 1

def dequeue(cola):
    if cola.tamanio == 0:
        raise RuntimeError("no se puede remover un elemento de la cola vacia")
    else:
        nodo_a_devolver = cola.frente
        cola.frente = nodo_a_devolver.siguiente
        if (cola.frente is None):
            cola.final = None
        cola.tamanio -= 1
        return nodo_a_devolver
    
def is_empty(cola):
    return (cola.tamanio == 0)

##--- implementar la funcion imprimir_cola
##-- usando el atributo tamanio de la cola
def imprimir_cola(cola):
    if cola.tamanio == 0:
        print("la cola esta vacia")
    else:
        nodo = cola.frente
        contador = 0
        while (contador < cola.tamanio):
            print(nodo.dato)
            nodo = nodo.siguiente
            contador += 1

##-- funcion primero()
def first(cola):
    return (None if cola.tamanio == 0 else cola.frente.dato)

#---- pruebas de funcionamiento de la cola ----#   
cola1 = Cola()
enqueue(cola1, 1)
enqueue(cola1, 2)
enqueue(cola1, 3)
enqueue(cola1, 4)
print(f"al frente de la cola esta el: {cola1.frente.dato}")
print(f"al final de la cola esta el: {cola1.final.dato}")
#print(f"remuevo el primer elemento de la cola: {dequeue(cola1).dato}")
#print(f"remuevo el segundo elemento de la cola: {dequeue(cola1).dato}")
#print(f"remuevo el tercero elemento de la cola: {dequeue(cola1).dato}")
#print(f"remuevo el cuarto elemento de la cola: {dequeue(cola1).dato}")
imprimir_cola(cola1)
print(f"el tamaño de la cola es: {cola1.tamanio}")
print(f"remuevo el quinto elemento de la cola: {dequeue(cola1).dato}")