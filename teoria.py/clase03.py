
"""
Resumen de Funciones, Modularidad y Alcance de Variables en Python
Basado en el material de la clase 3.
"""

# ========================
# FUNCIONES BÁSICAS
# ========================

# Definición simple de función

def saludar():
    """Imprime un saludo simple."""
    print("Hola mundo!")

saludar()

# Función que devuelve un valor

def obtener_saludo():
    """Retorna un saludo en lugar de imprimirlo."""
    return "Hola mundo!"

mensaje = obtener_saludo()
print(mensaje)

# ========================
# PARÁMETROS: Copia vs Referencia
# ========================

# Parámetro por copia (inmutable)
def incrementar(valor, cantidad):
    return valor + cantidad

numero = 5
nuevo_numero = incrementar(numero, 3)
print(numero)  # 5
print(nuevo_numero)  # 8

# Parámetro por referencia (mutable)
def agregar_elemento(lista, elemento):
    lista.append(elemento)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 4)
print(mi_lista)  # [1, 2, 3, 4]

# ========================
# ALCANCE DE VARIABLES (Scope)
# ========================

# Variable global
x = 10

def mostrar_global():
    print(x)  # Puede acceder

mostrar_global()

# Modificar variable global

def cambiar_global():
    global x
    x = 20

cambiar_global()
print(x)  # 20

# Uso de nonlocal en funciones anidadas

def externa():
    y = 5  # Variable local a la función externa
    def interna():
        nonlocal y  # Permite modificar la variable 'y' de la función externa
        y = 10  # Cambia el valor de 'y' en la función externa
    interna()
    print("Valor de y dentro de externa:", y)  # Muestra el valor modificado de 'y'

externa()

# ========================
# ARGUMENTOS POSICIONALES Y ASIGNADOS
# ========================

def mostrar_datos(nombre, edad=18):
    print(f"Nombre: {nombre}, Edad: {edad}")

mostrar_datos("Ana")  # Usa edad por defecto
mostrar_datos("Juan", edad=25)  # Asigna edad

# ========================
# GENERADORES Y YIELD (yield: Funciones que no retornan todo de una vez, sino que "generan" valores uno a uno con yield.Ahorran mucha memoria comparado con listas normales.)
# ========================

def generador_cuadrados(n):
    """Genera los cuadrados de los números desde 0 hasta n-1."""
    for i in range(n):
        yield i ** 2

for cuadrado in generador_cuadrados(5):
    print(cuadrado)

# ========================
# FUNCIONES RECURSIVAS
# ========================

# Factorial de un número

def factorial(n):
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))

# Fibonacci recursivo

def fibonacci(n):
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci de 6:", fibonacci(6))

# ========================
# DOCUMENTAR FUNCIONES
# ========================

def funcion_documentada():
    """Esta función está correctamente documentada para el comando help."""
    return True

help(funcion_documentada)