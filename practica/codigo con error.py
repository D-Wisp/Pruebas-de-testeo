def calcular_promedio(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    promedio = suma / len(numeros)
    return promedio

numeros = input("Ingresá una lista de números separados por comas: ")
numeros = numeros.split(",")
numeros = [int(n) for n in numeros]

if numeros:
    promedio = calcular_promedio(numeros)
    print("El promedio es: " + str(promedio))
else:
    print("No se ingresaron números válidos.")