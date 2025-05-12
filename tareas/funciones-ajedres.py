def getChessSquareColor():
    y = int(input("Ingrese la fila (0-7): "))
    x = int(input("Ingrese la columna (0-7): "))
    if y < 0 or y > 7 or x < 0 or x > 7:    
        raise TypeError("Las coordenadas deben estar entre 0 y 7")
    
    if (x + y) % 2 == 0:    
        color1 = "blanco"
        color2 = "negro"
    else:
        color1 = "negro"
        color2 = "blanco"  
    return color1, color2

color1, color2 = getChessSquareColor()
print(f"El color de la casilla es: {color1}")
print(f"El color de la casilla es: {color2}")

