serie = "N-02"

# if serie == "N-01":
#     print("Samsung")
# elif serie == "N-02":
#     print("Nokia")
# elif serie == "N-03":
#     print("Mootorola")
# else:
#     print("No se encontro")

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Mootorola")
    case _:
        print("No se encontro")


cliente = {"nombre": "Federico",
           "edad": 50,
           "ocupacion": "instructor"}

pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Keanu Reeves",
                              "director": "Lana y Lily Wachowski"}}

libro = {"titulo": "1984",
         "autor": "George Orwell"}

elementos = [cliente, pelicula, libro]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("este es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("este es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("unknown")