f = open("clase2828.txt" , "w")

for i in range(0, 25):
    f.write(f"{i}\n")  
f.close()

f2 = open("clase2828.txt", "r")

for linias in f2.readlines():
    print(linias, end='')
f2.close()

f3 = open("clase2828.txt", "a")
f3.write('Linea agregada 1')
f3.write('\n')
f3.write('Linea agregada 2')
f3.close()

with open("clase2828.txt", "w") as f4:
    f4.write('Sobre escribiendo archivo')
    
# While que pida una palabra al usuario
# si el usuario ingresa 'TERMINAR' -> Cierra el archivo y finaliza ejecución
# si no, guarda la palabra seguida de un salto de línea en el archivo
