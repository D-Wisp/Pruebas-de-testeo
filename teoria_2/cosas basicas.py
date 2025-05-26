# resumen_basico_python.py

# ✅ VARIABLES Y TIPOS DE DATOS
nombre = "Ana"
edad = 20
altura = 1.65
es_estudiante = True

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?", es_estudiante)

# ✅ ENTRADA Y SALIDA
usuario = input("¿Cómo te llamás? ")
print("Hola", usuario)

# ✅ CONDICIONALES
numero = int(input("Ingresá un número: "))
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")

# ✅ BUCLES
# FOR
print("Contando del 1 al 5:")
for i in range(1, 6):
    print(i)

# WHILE
contador = 0
while contador < 3:
    print("Intento", contador + 1)
    contador += 1

# ✅ LISTAS
frutas = ["manzana", "banana", "pera"]
print("Primera fruta:", frutas[0])
frutas.append("naranja")
print("Lista actualizada:", frutas)

# Recorrer una lista
for fruta in frutas:
    print("Fruta:", fruta)

# ✅ FUNCIONES
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Sofía")

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("La suma es:", resultado)

# ✅ OPERADORES
x = 10
y = 3
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y)
print("Módulo (resto):", x % y)

# ✅ MANEJO DE ERRORES
try:
    numero = int(input("Ingresá un número: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Eso no es un número válido.")

# ✅ EXTRA: verificar par/impar
def es_par(n):
    return n % 2 == 0

print("¿8 es par?", es_par(8))


#✅ El archivo incluirá:
#Variables

#Tipos de datos (str, int, float, bool)

#Entrada y salida (input(), print())

#Condicionales (if, else, elif)

#Bucles (for, while)

#Listas (crear, acceder, recorrer, métodos)

#Funciones (def)

#Operadores comunes

#Un poco de manejo de errores (try, except)

#Ejemplos breves para cada cosa