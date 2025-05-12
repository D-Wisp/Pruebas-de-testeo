usuario = "nahuel"
contraseña = "1234"
while usuario != "nahuel":
    usuario = input("introduce tu nombre de usuario: ")
    if usuario == "nahuel":
        print("usuario correcto")
        break
    else: 
        print("usuario incorrecto, vuelve a intentarlo")
intentos = 3
intentos_hechos = 0
while intentos > 0 and intentos_hechos < 3:
    intentos_hechos += 1
    contraseña_usuario = input("Introduce la contraseña: ")
    if contraseña_usuario == contraseña:
        print("correcto, has podidos entrar")
        break
    else:
        intentos -= 1
        print(f"contraseña incorrecta, te quedan {intentos} intentos")
if intentos == 0:
    print("Has agotado todos los intentos, prueba mas tarde")
    
     