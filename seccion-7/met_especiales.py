class CD:
    def __init__(self, autor, titulo, nro_canciones):
        self.autor = autor
        self.titulo = titulo
        self.nro_canciones = nro_canciones
    
    def __str__(self):
        return f"CD {self.titulo} de {self.autor}"


cd_1 = CD("Pink Floyd", "The Wall", 24)

print(str(cd_1))