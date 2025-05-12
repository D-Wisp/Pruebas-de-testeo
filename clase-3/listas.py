# LISTA

lista1 = [0, -6, -2.5, 'A', 'B', [5, 4]]
#Agregar al final 
lista1.append('pepe')
lista1.remove([5, 4])
print(lista1)
elemento = lista1.pop(-1)
print(f"Elemento eliminado: {elemento}")
lista1.insert(1, 'Juanito Perez')
print(lista1)
lista1.reverse()
print(lista1)

lista2 = [90, 80, 2.0, 69, 0]
lista2.sort()
print(lista2)

lista3 = ['Q', 'LL', 'Ñ', 'V', 'T']
lista3.sort()
print(lista3)

letra = lista3[2]
print(letra)
lista3[3] = 'U'
print(lista3)

