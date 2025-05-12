#################
#
#practica combianado lo dado en las ultimas clases.
#estoy tratando de hacer un ahorcado por turnos, el cual empezaria con los jugadores registrando un nick y luego el programa le da la bienvenida.
#dando paso a que la partida comience, el programa elige una palabra al azar dentro de una lista y los jugadore deben de adivinarla.
#
#################

import time

jugadores = {}

for i in range(1):
    jugadores["jugador 1"] = input("jugador 1 ingresa tu nick: ")
    print(jugadores["jugador 1"])
    

for i in range(1):
    jugadores["jugador 2"] = input("jugador 2 ingresa tu nick: ")
    print(jugadores["jugador 2"])
    
    
if jugadores and jugadores["jugador 2"]: 
    print(f"el nombre de los jugadores son: {jugadores['jugador 1']} y {jugadores['jugador 2']}")
    print("Sean bienvenidos al juego!")
    print("El juego comenzara en unos instantes, preparados?")

time.sleep(10)
print("Empezamos!")
time.sleep(2)
print("hoy jugaran el ahorcado")
time.sleep(2)
print("el cual consiste en adivinar la palabra oculta")
time.sleep(2)
print("quien logre sacar la palabra antes gana el juego!")
time.sleep(2)
print("¿están listos?")

palabra_random = {"chaja", "obrero", "brenda", "tralalerotralala", "agarrini la palini", "flor", "maximo", "cafe", "ingles", "bolita","nada", "familia"}
vidas = 6
palabra = palabra_random.pop() #esta linia lo que hace es agarrar la lista y elegir una palabra al azar.
letras_adivinadas = ["_" for _ in palabra]

letras_adivinadas = ["_"] * len(palabra)
print(letras_adivinadas)
print("la palabra tiene", len(palabra) , "letras")
print("cada jugador tiene 6 vidas")
print(f"turno de jugador 1")

turnos = 1


while vidas > 0 and "_" in letras_adivinadas:
    jugador_actual = jugadores[f"jugador {turnos}"]
    print(f"turno de {jugador_actual}") #esta linia muestra de quien es el turno y lo muestra con el nombre del jugador.
    print("tienes 10 segundos para escribir una letra...")
    start = time.time()
    letras_del_jugador = input(f"recuerda que tiene {vidas} intentos. " f"introduce una letra ===> ").lower()
    tiempo_transcurrido = time.time() - start
    
    if tiempo_transcurrido > 10:
        print(f"tu tiempo ya paso {tiempo_transcurrido: .2f}, pierdes una vida")
        vidas -= 1
        
        turnos = 2 if turnos == 1 else 1 #esta linia lo q hace es alternar entre jugadores, si el jugador 1 falla es el turno del jugador 2 y viceversa.
        continue
    
    
    if letras_del_jugador in palabra:
        print("Correcto!")
        for index, letra in enumerate(palabra):
            if letra == letras_del_jugador:
                letras_adivinadas[index] = letras_del_jugador
    
    
    else:
        print("letra incorrecta")
        vidas -= 1
        print(f"jugador {turnos} te quedan {vidas} intentos.\n")
        print("letras incorrectas: ", " ".join(letras_adivinadas))   
        print("ingresa otra letra ===> ")
            

                        
    if "_" not in letras_adivinadas:
        print(f"felicidades {jugador_actual} lo lograste :)")
    print(" ".join(letras_adivinadas))
    turnos = 2 if turnos == 1 else 1
#el sistema de progreso + la palabra + el sistema de vidas ya funcionan. ya agregue el sistema de turnos, ahora cada jugador tiene su turno el cual es de 10 seg para escribir la letra.
#cosas a mejorar: el sistema de vidas sigue descontando aunque el jugador 1 falle o el jugador 2 falle, debo de de hacer q cada juagador tenga sus vidas independientemente.
