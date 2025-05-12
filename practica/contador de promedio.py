def calcular_promedio():
    notas = []

    cantidad_notas = int(input("¿Cuántas notas hay? "))

    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    promedio = sum(notas) / len(notas)

    print(f"El promedio de notas es: {promedio:.2f}")

calcular_promedio()