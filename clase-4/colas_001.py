class Cola:
    ''''implementacion de una cola en python, usando listas'''
    def __init__(self):
        self.elementos = []
        
    def is_empy(self):
        return (len(self.elementos) == 0)
    
    def len(self) -> bool:
        return len(self.elementos)
    
    def enqueue(self, nuevo_elemento):
        '''push - encolar'''
        self.elementos.append(nuevo_elemento)
        
    def dequeue(self):
        '''pop - desencolar'''
        if (len(self.elementos) == 0):
            return None
        else:
            return self.elementos.pop(0)
        
    def first(self):
        if len(self.elementos) == 0:
            return None
        else:
            return self.elementos[0]
        
        
cola1= Cola()
print(f"La cantidad de elementos de la cola es: {cola1.len()}")
print(f"cola esta vacion?{cola1.is_empy()}")
cola1.enqueue('A')
cola1.enqueue('B')
cola1.enqueue('C')
cola1.enqueue('D')
print(f"La cantidad de elementos de la cola es: {cola1.len()}")
print(f"cola esta vacion?{cola1.is_empy()}")
print(f"El primer elemento de la cola es: {cola1.first()}")
print(f"saco el primer elemento: {cola1.dequeue()}")
print(f"La cantidad de elementos de la cola es: {cola1.len()}")


## Escribir un programa que use nuestra pila o cola, y use los metodos implmentados.
## Tiene que escribir n cantidad de elementos.
## Los agrega {push / enqueue}
## Usando un while, los va sacando y mostrando.