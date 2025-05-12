def mayor_y_menor(*numeros):
    if len(numeros) == 2:
        if isinstance(numeros[0], int) and isinstance(numeros[1], int):
            print("Ambos argumentos son enteros")
    numerosMayores = max(numeros)
    numerosMenores = min(numeros)
    return numerosMayores, numerosMenores

numerosMayores, numerosMenores = mayor_y_menor(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Mayor:", numerosMayores, "Menor:", numerosMenores)
resultado = mayor_y_menor(numerosMayores, numerosMenores)
print(resultado)