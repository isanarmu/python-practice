# principal.py
# Módulo principal con la lógica del turnero de farmacia

from numeros import obtener_turno_perfumeria, obtener_turno_farmacia, obtener_turno_cosmeticos


def mostrar_menu():
    """
    Muestra el menú de opciones disponibles al cliente.
    """
    print("\n" + "="*40)
    print("SISTEMA DE TURNOS - FARMACIA")
    print("="*40)
    print("Seleccione el área a la que desea dirigirse:")
    print("\n1. Perfumería")
    print("2. Farmacia")
    print("3. Cosméticos")
    print("4. Salir")
    print("="*40 + "\n")


def procesar_opcion(opcion):
    """
    Procesa la opción seleccionada por el usuario y asigna un turno.
    
    Args:
        opcion: Número de opción seleccionada (1-4)
    
    Returns:
        True si el usuario elige continuar, False si elige salir
    """
    if opcion == "1":
        print("Ha seleccionado: Perfumería")
        obtener_turno_perfumeria()
        return True
    
    elif opcion == "2":
        print("Ha seleccionado: Farmacia")
        obtener_turno_farmacia()
        return True
    
    elif opcion == "3":
        print("Ha seleccionado: Cosméticos")
        obtener_turno_cosmeticos()
        return True
    
    elif opcion == "4":
        print("¡Gracias por utilizar nuestro sistema de turnos! ¡Hasta luego!")
        return False
    
    else:
        print("⚠️  Opción inválida. Por favor, ingrese 1, 2, 3 o 4.")
        return True


def solicitar_otro_turno():
    """
    Pregunta al cliente si desea sacar otro turno.
    
    Returns:
        True si desea continuar, False si desea salir
    """
    while True:
        respuesta = input("¿Desea sacar otro turno? (s/n): ").lower().strip()
        if respuesta in ["s", "si"]:
            return True
        elif respuesta in ["n", "no"]:
            return False
        else:
            print("⚠️  Respuesta no válida. Por favor, ingrese 's' o 'n'.")


def main():
    """
    Función principal que controla el flujo del programa.
    Ejecuta un loop que permite al usuario sacar turnos hasta que decide salir.
    """
    print("\n¡Bienvenido al sistema de turnos de la farmacia!")
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").strip()
        
        # Procesar la opción seleccionada
        continuar_programa = procesar_opcion(opcion)
        
        # Si es opción 4 (Salir), se detiene el programa
        if opcion == "4":
            break
        
        # Si fue una opción válida (1, 2, 3), pregunta si desea otro turno
        if continuar_programa and opcion in ["1", "2", "3"]:
            continuar = solicitar_otro_turno()
            if not continuar:
                print("¡Gracias por utilizar nuestro sistema de turnos! ¡Hasta luego!")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
