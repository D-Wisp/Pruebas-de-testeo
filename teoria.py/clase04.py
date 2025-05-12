
"""
Resumen de:
- Programación Orientada a Objetos (OOP)
- Módulos en Python
- Manejo de Excepciones
"""

# ============================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (OOP)
# ============================================

# Definición de una clase simple
class Persona:
    """Ejemplo básico de clase."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia
persona1 = Persona("Ana", 30)
persona1.saludar()

# Duck Typing: Python no chequea tipos estrictamente
class Pato:
    def nadar(self):
        print("El pato nada.")

def hacer_nadar(objeto):
    objeto.nadar()

pato = Pato()
hacer_nadar(pato)

# ============================================
# MÓDULOS EN PYTHON (los mas comunes son: math, numpy, random)
# ============================================

# Importar módulo completo
import math
print(math.pi)  # Constante pi

# Importar módulo con alias
import numpy as np
matriz = np.array([[1, 2], [3, 4]])
print(matriz)

# Importar funciones específicas
from random import random, randrange
print(random())
print(randrange(5))

# ============================================
# EXCEPCIONES EN PYTHON (raise: lanza manualmente un error, assert: chequea condiciones, try-except - else: maneja errores)
# ============================================

# Uso de try - except - else
try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debe ingresar un número entero.")
else:
    print(f"El resultado es: {resultado}")

# Levantar errores manualmente
n = 5
d = 0
if d == 0:
    raise ValueError("El denominador debe ser distinto de '0'")

# Aserciones para validaciones internas
x = 5
assert x > 0, "x debe ser positivo"

# Ejemplo de error común: IndexError
lista = [1, 2, 3]
try:
    print(lista[5])
except IndexError:
    print("Índice fuera de rango.")

# Error semántico típico (solución correcta usando copy)
L = [1, 32, 3]
M = L.copy()  # No M = L
L.pop(1)
print("L=", L, "M=", M)

# ============================================
# FIN DEL RESUMEN
# ============================================

"""
Este resumen cubre:
- OOP: Definición de clases, atributos, métodos, self, y duck typing.
- Módulos: Importaciones y ejemplos de math, numpy y random.
- Excepciones: Tipos de errores, manejo de errores y ejemplos prácticos.
"""


#Resumen de lo mas importante de la clase 4:
#1. Programación Orientada a Objetos (OOP)
#Objeto: Instancia de una clase.

#Clase: Define atributos (variables) y métodos (funciones).

#Principios:
#Modularidad: Dividir en partes independientes.
#Abstracción: Ocultar detalles internos.
#Encapsulación: Proteger datos (usando _nombre por convención).
#Duck Typing: "Si camina como un pato..." — no se chequean tipos explícitos, importa el comportamiento.
#Self: Referencia a la propia instancia.
#Constructor __init__: Método especial para inicializar nuevos objetos.
#Sobrecarga de operadores: Podemos redefinir operadores como +, -, etc.

#2. Módulos en Python
#Módulo: Archivo .py con funciones, clases, variables, etc.

#Importaciones:
#import modulo
#import modulo as alias
#from modulo import objeto
#from modulo import *

#Módulos comunes:
#math, random, numpy, scipy.
#Importar propios módulos: Encapsular tu código y reutilizarlo.

#3. Errores y Excepciones
#Errores sintácticos: Impiden correr el programa (ej: IndentationError, SyntaxError).

#Errores semánticos: El programa corre pero produce resultados incorrectos.

#Manejo de excepciones:
#raise: Lanza manualmente un error.
#assert: Verifica condiciones.
#try - except - else: Captura y maneja errores.

#Errores comunes:
#IndexError, NameError, ValueError, TypeError, OverflowError.

#Depuración:
#Usar print(), assert, y depuradores.