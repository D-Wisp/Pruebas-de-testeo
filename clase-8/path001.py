from pathlib import Path

ruta1 = Path('./no_existe.txt')
ruta2 = Path('./clase-8/path001.py')
ruta3 = Path.cwd() / 'clase-8' 

print(f"el directorio actual de trabajo es: {Path.cwd()}")
print(f"Mi carpeta home es: {Path.home()}")
print()
print(f"ruta 1 apunta a {ruta1}")
print(f"existe ruta 1? {ruta1.exists()}")
print(f"ruta 1 es un directorio? {ruta1.is_dir()}")
print(f"el nombre es: {ruta1.name}")
print(f"la extencion es: {ruta1.suffix}")
print(f"los parents es: {ruta1.parents}")
print(f"si aplico el metodo resolve() obtengo: {ruta1.resolve()}")
print()
print(f"ruta 2 apunta a {ruta2}")
print(f"existe ruta 2? {ruta2.exists()}")
print(f"ruta 2 es un directorio? {ruta2.is_dir()}")
print()
print(f"ruta 3 apunta a {ruta3}")
print(f"existe ruta 3? {ruta3.exists()}")
print(f"ruta 3 es un directorio? {ruta3.is_dir()}")
print(f"los parents es: {ruta3.parents}")
print(f"si aplico el metodo resolve() obtengo: {ruta3.resolve()}")


# escribir un programa que le pida al usuario
# El nombre primero
# la extencion del archivo despues 
# crear un path
# y mostrar por pantalla si el archivo existe
# si la ruta es un directorio