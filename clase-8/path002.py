from pathlib import Path

directorio1 = Path('./directorio_nuevo')
print(f"existe directorio_nuevo? {directorio1.exists()}")

if directorio1.exists():
    directorio1.rmdir() # remove directory

try:
    directorio1.mkdir() # Make directory
    print(f"existe directorio_nuevo? {directorio1.exists()}")
except Exception as e:
    print(f"no se puede crear el directorio porque: {e}")
    

# Escribir un programa que pida al usuario un nombre de directorio
# Si el directorio existe lo borra
# Sino existe lo crea