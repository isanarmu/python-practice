from pathlib import Path
# abrir obejo path con metodos distinots | no hace falta open oclose
carpeta = Path("C:\\Users\\Irene\\Desktop\\Probando rutas\\vesina.txt.txt")
base = Path.home()

ruta = Path.home() / "Curso Python" / "Día 6" / "practicas_path.py"
print(f"esto es la base: ", base)

print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
print(carpeta.read_text())
print(carpeta.exists())