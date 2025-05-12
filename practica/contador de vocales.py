def contar_vocales(palabra):
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra.lower() in vocales:
            contador += 1
    return contador
palabra = (input("Escribe una palabra: "))
resultado = contar_vocales(palabra)
print(f"La palabra '{palabra}' tiene {resultado} vocales")
   