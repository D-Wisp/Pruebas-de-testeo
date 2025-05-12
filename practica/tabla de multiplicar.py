def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
n = int(input("Escribe un número: "))
tabla_multiplicar(n)
