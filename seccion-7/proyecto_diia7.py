

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

def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta  = input("Numero de cuenta: ")
    balance = float(input("Balance inicial: ").replace(" ", ""))

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)

    return cliente
cliente = crear_cliente()
print(cliente)