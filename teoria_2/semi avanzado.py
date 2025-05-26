#✅ Este archivo incluye:
#Funciones con parámetros y return

#Listas con condicionales

#Diccionarios

#Uso de for con enumerate

#Uso de zip()

#Validaciones de entrada

#Mini desafío: promedio de estudiantes con control de errores

#######
# ejercicios_semi_avanzados.py
########

# ✅ FUNCIONES CON RETURN Y PARÁMETROS
def es_mayor_de_edad(edad):
    return edad >= 18

edad_usuario = int(input("Ingresá tu edad: "))
if es_mayor_de_edad(edad_usuario):
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

# ✅ LISTAS Y CONDICIONALES
numeros = [5, 12, 7, 20, 1, 3]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print("Números pares:", pares)

# ✅ DICCIONARIOS
persona = {
    "nombre": "Lucía",
    "edad": 30,
    "ciudad": "Rosario"
}

print(f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['ciudad']}.")

# ✅ USO DE ENUMERATE
animales = ["gato", "perro", "pez"]
for i, animal in enumerate(animales):
    print(f"{i+1}. {animal}")

# ✅ USO DE ZIP
nombres = ["Ana", "Juan", "Pedro"]
notas = [7, 9, 6]

for nombre, nota in zip(nombres, notas):
    print(f"{nombre} sacó {nota}")

# ✅ FUNCIONES + VALIDACIONES + LISTAS
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def ingresar_notas():
    notas = []
    while True:
        entrada = input("Ingresá una nota (o escribí 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Eso no es un número válido.")
    return notas

print("\n🔢 Carga de notas de estudiante")
notas_cargadas = ingresar_notas()
prom = calcular_promedio(notas_cargadas)
print(f"Promedio final: {prom:.2f}")
