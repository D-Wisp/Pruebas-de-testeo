palabra_random = 'nublado'
vidas = 7
letras_adivinadas = ["_" if letra != " " else " " for letra in palabra_random]
ahorcado = [
    """
    
    +---+=
          |  
          |     
          |    
          |
          |    
    ======|
    
    
    """
    ,
    
    """
    
    +---+=
      O   |  
          |     
          |    
          |
          |    
    ======|
    
    """
    ,
    
    """ 
    
    +---+=
      O   |  
      |   |     
          |    
          |
          |    
    ======|
    
    
    
    """
    ,
    """
    
     +---+=
      O   |  
      |   |     
      |   |    
          |
          |    
    ======|
    
    """
    
    ,
    
    """
    
     +---+=
      O   |  
     /|   |     
      |   |    
          |
          |    
    ======|
    
    """
    ,
    
    """
    
     +---+=
      O   |  
     /|\  |     
      |   |    
          |
          |    
    ======|
    
    """
    ,
    
    """
    
     +---+=
      O   |  
     /|\  |     
      |   |    
     /    |
          |    
    ======|
    
    """
    ,
    
    
    """
    
     +---+=
      O   |  
     /|\  |     
      |   |    
     / \  |
          |    
    ======|
    
    """
]  #El dibujo esta definido en una lista, se ejecuta junto al print() de la linia 129.... la cual esta enlasada al sistema de vidas.
while vidas > 0 and "_" in letras_adivinadas:
    letras_del_jugador = input(f"Tienes {vidas} intentos: " + "Introduce una letra ===> ").lower()
    
    if letras_del_jugador in palabra_random:
        for index, letra in enumerate(palabra_random):
            if letra == letras_del_jugador:
                letras_adivinadas[index] = letras_del_jugador
        print("Correcto!") # Acordate que los print tienen q estar bien posicionados para que funcione bien el codigo.
    else:
        vidas -= 1
    print(" ".join(letras_adivinadas)) # Los print siempre deben de estar conectado con el else, if o for (osea debe esta conectado con el | para q fucionen correctamente.)   
    print(f"letra incorrecta te quedan {vidas} intentos.\n")          
    print(ahorcado[7 - vidas])                    
    if "_" not in letras_adivinadas:
                print("felicidades lo lograste :)")


print(ahorcado[7 - vidas])