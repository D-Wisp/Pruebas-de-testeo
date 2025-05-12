#DICCIONARIOS 

dict1 = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
dict1['clave2']
print(dict1['clave2'])
dict1['clave_nueva'] = 'Movistar2.0'
print(dict1['clave_nueva'])

dict1.get('clave_nueva')
print(dict1.get('clave_nueva'))

valor_eliminado = dict1.pop('clave1')
print(valor_eliminado)

print(dict1)

print(len(dict1))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

