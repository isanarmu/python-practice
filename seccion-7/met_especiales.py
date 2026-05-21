class CD:
    def __init__(self, autor, titulo, nro_canciones):
        self.autor = autor
        self.titulo = titulo
        self.nro_canciones = nro_canciones
    
    def __str__(self):
        return f"CD {self.titulo} de {self.autor}"
    def __len__(self):
        return self.nro_canciones
    def __del__(self):
        print("CD eliminado")


cd_1 = CD("Pink Floyd", "The Wall", 24)

print(len(cd_1))