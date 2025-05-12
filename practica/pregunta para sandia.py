import time

preguntas = ["tienes novia?", "que paso ese 5 de abril?", "kevin es peruano?", "chitearla o ser peruano?"]
print(("bienvenido sandia!!"))
time.sleep(3)
print("te hare una serie de preguntas y quiero q respondas con si o no")
time.sleep(2)
print("preparado?")

for pregunta in preguntas:
    respuesta = input(pregunta + "si / no: ")
    print("tu respuesta es: " + respuesta)
    time.sleep(1)
    if respuesta == "si":
        print("Bien pensado")
    else:
        print("prefiero no decir nada (maldito bolita)")
        time.sleep(1)
        
