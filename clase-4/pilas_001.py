class Pila:
    '''estructura pila implementada con una lista python'''
    def __init__(self):
        self.elementos = []
     
    def len(self) -> int:
        '''devuelve el número de elementos en la pila'''
        return len(self.elementos)        

    def is_empy(self) -> bool:
        '''devuelv true si la lista esta vacia'''
        return len(self.elementos) == 0

    def push(self, nuevo_elemento):
        '''agrega un elemento en el top de la pila'''
        self.elementos.append(nuevo_elemento)
        
    def pop(self):
        '''remueve y devuelve el ultimo elemento'''
        if (len(self.elementos) == 0):
            return None
        else:
            return self.elementos.pop()#devuelve el ultimo elemento de la lista
    
    def top(self):
        '''muestra el ultimo elemento sin eliminarlo'''
        if (len(self.elementos)== 0):
            return None
        else:
            return self.elementos[-1]
        
    def list_elemts(self):
        return self.elementos[::-1]#devuelve el ultimo elemento de la lista
   
        
pila1 = Pila()
print(f"La cantidad de elementos de la pila es:{pila1.len()}")
print(f"La pila esta vacia? {pila1.is_empy()}")
pila1.push('A')
pila1.push('B')
pila1.push('C')
print(f"La cantidad de elementos de la pila es: {pila1.len()}")
print(f"La pila esta vacia? {pila1.is_empy()}")
print(f"el ultimo elemento ingresado a la pila es: {pila1.top()}")
print(f"remuevo el ultimo elemento de la pila, y lo muestro: {pila1.pop()}")
print(f"la cantidad de elementos de la pila es: {pila1.len()}")
print(pila1.list_elemts())