# escribir un programa que le pida al usuario
# El nombre primero
# la extencion del archivo despues 
# crear un path
# y mostrar por pantalla si el archivo existe
# si la ruta es un directorio
from pathlib import Path
usuario = input("ingrese el nombre del archivo: ")
extencion = input("ahora la extencion de su archivo: ")
ruta = Path(f"{usuario}.{extencion}")


print(f"el directorio actual de trabajo es: {Path.cwd()}")
print(f"la ruta de tu archivo es: {ruta}")
print(f"existe la ruta? {ruta.exists()}")
print(f"la extencion de tu archivo es: {ruta.suffix}")
print(f"La ruta es un directorio? {ruta.is_dir()}")