palabra_a_adivinar = "BOB EL CONSTRUCTOR"
CANTIDAD_DE_VIDAS = 6
letras_adivinadas = ["_" if letra != " " else " " for letra in palabra_a_adivinar]
for i in range(0, CANTIDAD_DE_VIDAS):
    letras_del_usuario = input("Recuerda que tienes solo 6 intentos >> " + "Introduce una letra >> ")
    
    for letra in palabra_a_adivinar:
        if letra == letras_del_usuario:
            print(letra, end= ' ')
        else:
            print(' - ', end=' ') 
            print(letras_del_usuario) == [False] >= 0
            print(CANTIDAD_DE_VIDAS >= 0)
            
   