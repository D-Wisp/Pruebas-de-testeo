def division(dividendo, divisor):
    resultado = None
    try:
        dividendo = float(dividendo)
        divisor = float(divisor)
        resultado = float(dividendo) / float(divisor)
        
    except ValueError:
        print("no se puede convertir los valores")
    except ZeroDivisionError:
        print("no se puede dividir en 0")
    except Exception as e:
        print(f"algo salio mal... {e}")
    finally:
        return resultado
   
numero1 = input("Dividendo -> ")
numero2 = input("Divisor -> ")

print(division(numero1, numero2))

lista1 = [0, 8, 6, 7]
#print(lista1[100])
diccionario1 = {'uno': 1, 'dos': 2, 'tres': 3}
#print(diccionario1['cuatro'])