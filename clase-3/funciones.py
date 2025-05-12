def sumar(numero1: int, numero2: int) -> int:
   
     if isinstance(numero1 , int)or isinstance (numero1,float) and isinstance(numero2 , int):
        print("Ambos argumentos son enteros")
        return numero1 + numero2
     else:
         raise TypeError("Debe ingresar dos numeros enteros")


def multiplicar(numero1, numero2, multiplicar_por=2):
    return (numero1 + numero2) * multiplicar_por


def dividir(numero1, numero2, dividir_por=2):
    if dividir == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return (numero1 + numero2) / dividir_por

resultado = sumar(11.5, 3)
print(f"El resultado de la suma es: {resultado}")

resultado1 = multiplicar(3, 2)
resultado2 = multiplicar(5, 5, 10)
resultado3 = dividir(10, 5)
try:
    resultado4 = dividir(10, 0)
except ZeroDivisionError as e:
    print(e)
print(resultado3)
print(resultado1)
print(resultado2)