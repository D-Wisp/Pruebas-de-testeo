palabra = 'operador'
vidas = 10
letras_adivinadas = ["_" if letra != " " else " " for letra in palabra] #este es el sistema de casillas, lo que hace es ver cuantas letras hay en la palabra y poner esa cantidad en forma de ("_")

while vidas > 0 and "_" in letras_adivinadas: #este es un sistema de bucle, el cual hace q se repitan las condiciones del If y else, dependiendo de cual deberia efectuarse.
    letras_del_jugador = input(f"Solo tienes {vidas} vidas. " + "adjunta una letra >>").lower() # .lower () .upper () funcionan de las misma manera, una para minusculas y la otra para mayusculas, no importa si el jugador pone de una o otra manera su letra que eso se lo va dar de valido igual.
   
    if letras_del_jugador in palabra: #este sistema es un sistema de progreso el cual fuciona si el jugador adivina una letra en ves de poner el guio("_"), pone la letra.
        for index, letra in enumerate(palabra):
            if letra == letras_del_jugador:
                letras_adivinadas[index] = letras_del_jugador
        print("Correcto")   
    else: #este es el sistema de vidas, por cada letra mal le descuenta una vida al jugador.
        vidas -= 1           
    print(" ".join(letras_adivinadas))   
    print(f"Te quedan {vidas} intentos.\n") # esto lo que hace es decirle al jugador cuantos intentos le quedan al errar una letra. / la \n es un carácter de nueva línea (newline). 
    #la \n es un carácter de nueva línea (newline).Su función es hacer que el cursor pase a la siguiente línea después de imprimir el mensaje.
    #Va imprimir primero los "_" y abajo imprimira el print() de la linia 16.
                      
    if "_" not in letras_adivinadas: #este if lo que hace es ver si ya no quedan letras por adivinar y si no hay ejecuta el print.
        print("lo lograste")
   
#tarea comletada el dia 20/3/2025
#by: nahu :)
#Recuerda que el If y else son condicionales, lo cual cada uno tiene una funcion de si y no.... 
# Si una condicion se cumple ejecuta lo q esta dentro del if, si una condicion no se cumple ejecutara el else.
