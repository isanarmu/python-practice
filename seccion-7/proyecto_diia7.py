def inicio():
    cliente = crear_cliente()
    
    while True:
        print("\n" + str(cliente))
        print("\n¿Que desea hacer?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        opcion = input("Elige una opción:")

        if opcion == "1":
            cantidad = float(input("¿Cuánto quieres depositar?: "))
            cliente.depositar(cantidad)
            print("balance actualizado: {cliente.balance}")

        if opcion == "2":
            cantidad = float(input("¿Cuánto quieres retirar?: "))
            cliente.retirar(cantidad)
            print("balance actualizado: {cliente.balance}")
        if opcion == "3":
            print("Saliendo del programa...")
            break

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido        

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
    
    def retirar(self, cantidad_retirar):
        if cantidad_retirar <= self.balance:
            self.balance -= cantidad_retirar
        else:
            print("No tienes fondos suficientes.")
            
def crear_cliente():

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta  = input("Numero de cuenta: ")
    balance = float(input("Balance inicial: ").replace(" ", ""))

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)

    return cliente

inicio()