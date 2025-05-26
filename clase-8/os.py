import os
from pathlib import Path
import shutil

print(os.getcwd())
os.chdir(Path('./clase-8')) # Cambia al directorio clase-8
print(os.getcwd())
# os.copy(Path('./clase-7'), Path('./clase-8'))

shutil.copy(Path('./toria_1'), '.')

## Ejemplo
# Mostrar un menú para el usuario con las siguientes opciones:
# 1 - Listar todos los archivos
# 2 - Mostrar el directorio de trabajo actual
# 3 - Listar los archivos según condición (pedir la condición)
# 4 - Crear una nueva carpeta (si no existe)
# 5 - Borrar una carpeta (avisar si falla)
# 6 - Copiar un archivo con otro nombre (pedir al usuario el nombre y verificar que exista)
# 0 - Salir del Programa