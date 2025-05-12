texto_para_analizar = "Un anillo para dominarlos a todos"

print(len(texto_para_analizar))

harry_potter = 'WINGARDIUM LEVIOSA'
print('A' in harry_potter)

letras_a = 0
letras_no_a = 0

CANTIDAD_DE_VIDAS = 20

for i in range(0, CANTIDAD_DE_VIDAS):

 letra_del_usuario = input("ingrese una letra >>>  ")

 for letra in harry_potter:
    if letra == 'A' :
        letras_a += 1
    else:
        letras_no_a = letras_no_a + 1

print(f"En {harry_potter} encontre {letras_a} letras acertadas")
print(f"{harry_potter} encontre {letras_no_a} letras q no acertadas")