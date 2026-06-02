# numeros.py
# Módulo con generadores y decorador para el sistema de turnos de farmacia

# Generadores de turnos para cada área
def generador_turnos(letra):
    """
    Generador que produce números de turno con una letra inicial.
    
    Args:
        letra: Letra inicial del área (P, F, C)
    
    Yields:
        Número de turno en formato "LETRA-número"
    """
    numero = 0
    while True:
        numero += 1
        yield f"{letra}-{numero}"


# Crear generadores individuales para cada área
gen_perfumeria = generador_turnos("P")
gen_farmacia = generador_turnos("F")
gen_cosmeticos = generador_turnos("C")


# Decorador que envuelve el mensaje del turno
def mensaje_turno(funcion):
    """
    Decorador que añade un mensaje formateado alrededor del número de turno.
    
    El decorador muestra:
    - Mensaje inicial: "Su turno es:"
    - El número de turno (retorno de la función)
    - Mensaje final: "Aguarde y será atendido"
    """
    def envolvente():
        print("\n" + "="*40)
        print("Su turno es:")
        turno = funcion()  # Obtener el número de turno de la función
        print(turno)
        print("Aguarde y será atendido")
        print("="*40 + "\n")
        return turno
    
    return envolvente


# Funciones decoradas para obtener el siguiente turno de cada área
@mensaje_turno
def obtener_turno_perfumeria():
    """Obtiene el siguiente turno de Perfumería."""
    return next(gen_perfumeria)


@mensaje_turno
def obtener_turno_farmacia():
    """Obtiene el siguiente turno de Farmacia."""
    return next(gen_farmacia)


@mensaje_turno
def obtener_turno_cosmeticos():
    """Obtiene el siguiente turno de Cosméticos."""
    return next(gen_cosmeticos)
