# Escribir un programa que pida al usuario un nombre de directorio
# Si el directorio existe lo borra
# Sino existe lo crea
from pathlib import Path
user = input("porfavor ingrese el nombre del directorio: ")
directorio = Path(user)
if directorio.exists():
    directorio.rmdir()
    print(f"el directorio {directorio} a sido eliminado")
else:
    try:
        directorio.mkdir()
        print(f"el directorio {directorio} a sido creado")
    except Exception:
        print(f"el directorio ya existe")
