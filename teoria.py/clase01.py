# Estructuras de Control Básicas
#Secuencia: Instrucciones que se ejecutan una tras otra.

#Ejemplo:

X = 10  
Y = 5

#Decisión (if): Elegir entre dos opciones.
#Ejemplo:


if X > 0:  
    print("Positivo")  
else:  
    print("Negativo")  

# Note: (switch/casos): Elegir entre muchas opciones.
#Ejemplo:

edad = int(input("Ingrese la edad: "))

if edad < 10:
    print("Niño")
elif 10 <= edad <= 20:
    print("Adolescente")

# Repetición (for): Repetir un número fijo de veces.
for i in range(1, 11):
    print(i)

#Ejemplo:

for i in range(1, 11):  
    print(i)  

# Iteración (while): Repetir mientras se cumpla una condición.

#Ejemplo:

while X > 0:  
    print(X)  
    X = int(input("Ingrese un nuevo valor para X: "))  
