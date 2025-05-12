Palabra_a_adivinar = 'MECANICO'
CANTIDAD_DE_VIDAS = 6
letras_adivinadas = ["_" if letra != " " else " " for letra in Palabra_a_adivinar]
print(("M") + ("E") + ("C")+ ("A")+ ("N")+ ("I")+ ("C")+ ("O") in Palabra_a_adivinar)
for i in range(0, CANTIDAD_DE_VIDAS):
    letras_del_usuario = input(f"Recuerda que tienes {CANTIDAD_DE_VIDAS} intentos >> " + "introduce una letra >> ")
    
    for letra in Palabra_a_adivinar:
        if letra == letras_del_usuario:
                print(letra, end= '')
        else:
            print('_', end=' ')