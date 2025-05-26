#✅ Este archivo incluye:
#Funciones más estructuradas

#Uso de módulos (random, time)

#Diccionarios

#Listas dentro de listas

#Juego con turnos

#Validación de entrada

#Lógica de control

#🎮 Mini juego: Trivia de Cultura General por turnos
#Temas avanzados que vas a usar y entender:

#Modularización con funciones

#Diccionarios con preguntas/respuestas

#Turnos entre jugadores

#Contador de puntos

#Uso de random.shuffle() para mezclar preguntas

# trivia_avanzada_turnos.py
import random
import time

# ✅ Preguntas y respuestas (diccionario)
preguntas = [
    {"pregunta": "¿Cuál es la capital de Francia?", "opciones": ["París", "Madrid", "Roma"], "respuesta": "París"},
    {"pregunta": "¿Cuántos planetas hay en el sistema solar?", "opciones": ["8", "9", "7"], "respuesta": "8"},
    {"pregunta": "¿Quién escribió 'Cien años de soledad'?", "opciones": ["Borges", "Cortázar", "García Márquez"], "respuesta": "García Márquez"},
    {"pregunta": "¿Qué gas necesitamos para respirar?", "opciones": ["Oxígeno", "Hidrógeno", "Dióxido de carbono"], "respuesta": "Oxígeno"},
    {"pregunta": "¿Cuál es el resultado de 9x7?", "opciones": ["63", "72", "56"], "respuesta": "63"}
]

# ✅ Función para hacer una pregunta
def hacer_pregunta(pregunta, jugador):
    print(f"\n🎯 Turno de {jugador}")
    print("📝", pregunta["pregunta"])
    opciones = pregunta["opciones"]
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    while True:
        try:
            eleccion = int(input("Elegí la opción correcta (1-3): "))
            if 1 <= eleccion <= 3:
                return opciones[eleccion - 1] == pregunta["respuesta"]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Ingresá un número válido.")

# ✅ Juego principal
def jugar_trivia():
    print("👾 Bienvenidos a la Trivia de Cultura General 👾")
    jugador1 = input("Jugador 1, ingresá tu nombre: ")
    jugador2 = input("Jugador 2, ingresá tu nombre: ")
    jugadores = [jugador1, jugador2]
    puntos = {jugador1: 0, jugador2: 0}

    random.shuffle(preguntas)  # Mezclamos las preguntas

    turno = 0
    for pregunta in preguntas:
        jugador_actual = jugadores[turno % 2]
        correcta = hacer_pregunta(pregunta, jugador_actual)
        if correcta:
            print("✅ ¡Correcto!")
            puntos[jugador_actual] += 1
        else:
            print("❌ Incorrecto.")
        turno += 1
        time.sleep(1)

    print("\n🎉 Fin del juego 🎉")
    print(f"{jugador1}: {puntos[jugador1]} puntos")
    print(f"{jugador2}: {puntos[jugador2]} puntos")

    if puntos[jugador1] > puntos[jugador2]:
        print(f"🏆 ¡{jugador1} gana!")
    elif puntos[jugador2] > puntos[jugador1]:
        print(f"🏆 ¡{jugador2} gana!")
    else:
        print("🤝 ¡Empate!")

# ✅ Ejecutar el juego
if __name__ == "__main__":
    jugar_trivia()
