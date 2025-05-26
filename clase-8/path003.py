from pathlib import Path

ruta1 = Path('.')

for archivo in ruta1.iterdir():
  directorio = None
  if archivo.is_dir():
      directorio = '[DIR]'
  else:
        directorio = '[FILE]'
        print(f"archivo: {archivo} {directorio}")
        
print('-------- Archivos de texto --------')
for i in ruta1.glob('*.txt'):
    print(f"archivo: {i} [FILE]")
    
# Solicite al usuario un nombre o parte del nombre de una archivo
# Muestre las coincidencias
# indique si se trata de un archivo o directorio