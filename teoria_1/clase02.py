# Resumen Simplificado – Clase 2: Tipos de Datos

# ¿Qué es un tipo de dato?
# Es el tipo de valor que puede tener una variable y lo que se puede hacer con ese valor.

# Tipos de datos básicos (simples)
entero = 10              # int
decimal = 3.14           # float
complejo = 2 + 3j        # complex
texto = "Hola"           # str
booleano = True          # bool

# Operadores matemáticos
suma = 5 + 3             # 8
resta = 5 - 3            # 2
multiplicacion = 5 * 3   # 15
division = 5 / 2         # 2.5
division_entera = 5 // 2 # 2
resto = 5 % 2            # 1
potencia = 2 ** 3        # 8

# Operadores de comparación
igual = (5 == 5)         # True
distinto = (5 != 3)      # True
mayor = (5 > 3)          # True
menor = (5 < 3)          # False

# Operadores lógicos
resultado_and = True and False  # False
resultado_or = True or False    # True
resultado_not = not True        # False

# Conversión de tipos
a_entero = int("10")      # 10
a_decimal = float("3.5")  # 3.5
a_texto = str(123)        # "123"

# Tipos de datos compuestos

# Lista (mutable)
mi_lista = [1, 2, 3]
mi_lista.append(4)        # [1, 2, 3, 4]
mi_lista.pop()            # [1, 2, 3]

# Tupla (inmutable)
mi_tupla = (1, 2, 3)

# Conjunto (sin repetidos)
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)

# Diccionario (clave: valor)
mi_diccionario = {"nombre": "Ana", "edad": 20}
mi_diccionario["edad"] = 21

# Rango (inmutable)
rango = range(1, 10, 2)  # 1, 3, 5, 7, 9

# Comentarios
# Se usan con # y no afectan el código.

# Variables
# Nombres que almacenan valores, deben comenzar con letra o "_"
