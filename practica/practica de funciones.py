import time

def calculadora():
    print("Sea ustede Bienvenido mi estimado")
    print("Que es lo que desea hacer?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. salir")
    opciones = int(input("elija una opcion: "))
    while opciones < 1 or opciones >5:
        opciones = int(input("opcion no valida, elija una opcion: "))
        
    if opciones in [1, 2, 3, 4]:
        num1 = float(input("ingrese un numero: "))
        num2 = float(input("ingrese otro numero: "))
        
    if opciones == 1:
        resultado = num1 + num2
        time.sleep(2)
        print(f"la suma de {num1} + {num2} es: {resultado}")
    elif opciones == 2:
        time.sleep(2)
        resultado = num1 - num2
        print(f"la resta de {num1} - {num2} es: {resultado}")
    elif opciones == 3:
        resultado = num1 * num2
        time.sleep(2)
        print(f"la multiplicacion de {num1} * {num2} es: {resultado}")
    elif opciones == 4:
        if num2 == 0:
            print("no se puede dividir entre cero")
        else:
            resultado = num1 / num2
            time.sleep(2)
            print(f"la divicion de {num1} / {num2} es: {resultado}")

    
while True:
    opcion = input("¿Deseas realizar una cuenta? (si/no): ").lower()
    if opcion == "si":
        calculadora()
    elif opcion == "no":
        print("¡Gracias por usar la calculadora!")
        break
    else:
        print("Por favor, responde con 'si' o 'no'.")        
            
            
    