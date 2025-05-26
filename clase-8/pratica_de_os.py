## Ejemplo
# Mostrar un menú para el usuario con las siguientes opciones:
# 1 - Listar todos los archivos
# 2 - Mostrar el directorio de trabajo actual
# 3 - Listar los archivos según condición (pedir la condición)
# 4 - Crear una nueva carpeta (si no existe)
# 5 - Borrar una carpeta (avisar si falla)
# 6 - Copiar un archivo con otro nombre (pedir al usuario el nombre y verificar que exista)
# 0 - Salir del Programa
import os
from pathlib import Path
import shutil
def menu():
    print("\nMenu")
    print("Seleccione una opcion: ")
    print("1 - Listar todos los archivos")
    print("2 - Mostrar el directorio actual de trabajo")
    print("3 - Listar los archivos según condición")
    print("4 - Crear una nueva carpeta")
    print("5 - Borrar una carpeta")
    print("6 - Copiar un archivo con otro nombre")
    print("7 - salir / terminar")
    opciones = int(input("ingresa una opcion: "))
    while opciones < 1 or opciones > 7:
        opciones = int(input("opcion no valida, no sea menso q son solo 7 y no 10"))
    return opciones

def lista_de_archivos(): # te muestra en una lista los archivos y carpetas del directorio actual.
    ruta = Path('.')
    print("\nEsta es la lista de tus archivos: ")
    for archivo in ruta.iterdir():
        if archivo.is_dir():
            print(f"{archivo} [DIR]")
        else:
            print(f"{archivo} [FILE]")
        
def Directorio_actual(): # te muestra el directorio actual de trabajo.
    print(f"El directorio actual de trabajo es: {os.getcwd()}")
    
def listar_archivo_c(): # te muestra los archivos que cumplen con la condicion que le ingrasas al programa.
    condicion = input("ingrese la condicion del archivo (ejem: .txt, .py, etc):  )")
    archivos = [i for i in os.listdir() if i.endswith(condicion)]
    if archivos:
        print(f"los siguiente archivos cumplen la condicion: {condicion}")
        for archivo in archivos:
            print(archivo)
        else:
            print(f"No hay archivos con esa condicion: {condicion}")
            
def crear_carpeta(): # te deja crear carpetas nuevas en la ruta actual.
    nombre_carpeta = input("ingrese el nombre que desea para la nueva carpeta: ")
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        print(f"la carpeta {nombre_carpeta} fue creada exitosamente!")
    else:
        print(f"La carpeta o archivo con el nombre {nombre_carpeta} ya existe.")

def borrar_carpeta(): # Borra la carpeta que le vayas a indicar, si no existe o no es una carpeta te avisa.
    nombre_carpeta = input("ingrese el nombre de la carpeta: ")
    if os.path.exists(nombre_carpeta) and os.path.isdir(nombre_carpeta):
        try:
            os.rmdir(nombre_carpeta)
            print(f"la carpeta {nombre_carpeta} fue eliminada, ya no hay nada que hacer.")
        except OSError as e:
            print(f"No pudimos eliminar la carpeta {nombre_carpeta}. error: {e}")
        else:
            print(f"la carpeta {nombre_carpeta} no existe o no es una carpeta.")

def copiar_archivo(): # permite copiar un archivo que ya existe y le asigna un nuevo nombre.
    archivo_origen = input("ingrese el nombre del archivo a copiar: ")
    if os.path.exists(archivo_origen) and os.path.isfile(archivo_origen):
        nombre_del_nuevo_archivo = input("ingrese el nombre para el nuevo archivo: ")
        try:
           shutil.copy(archivo_origen, nombre_del_nuevo_archivo)
           print(f"El archivo {archivo_origen} fue copiado como {nombre_del_nuevo_archivo}.")
        except Exception as e:
           print(f"No se pudo copiar el archivo. Error: {e}")
        else:
            print(f"El archivo {archivo_origen} no existe o no es un archivo.")

def salir(): # termina de ejecutar el programa.
    print("saliendo del programa...")
    exit()

while True:
    opcion = menu()
    
    if opcion == 1:
        lista_de_archivos()
    elif opcion == 2:
        Directorio_actual()
    elif opcion == 3:
        listar_archivo_c()
    elif opcion == 4:
        crear_carpeta()
    elif opcion == 5:
        borrar_carpeta()
    elif opcion == 6:
        copiar_archivo()
    elif opcion == 7:
        salir()
        break
    
        