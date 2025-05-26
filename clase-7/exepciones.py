class ExceptionFlavio(Exception):
    pass


def dividir_con_divisor_par(dividendo, divisor):
    resultado = None
    try:
        numero1 = float(dividendo)
        numero2 = int(divisor)
        
        if divisor % 2 != 0:
            raise ExceptionFlavio("no es par el divisor") 
    
        resultado = numero1 / numero2
    
    except ValueError:
        print("no se puede convertir los numeros")    
    except ExceptionFlavio:
        print("no cumple las condiciones")
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    except Exception as e:
        print(f"ah ocurrido un error: {e}")
    finally:
        return resultado
    
    
numero1 = input("dividendo -> ")
numero2 = input("divisor -> ")
print(dividir_con_divisor_par(numero1, numero2))