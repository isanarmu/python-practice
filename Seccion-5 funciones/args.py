def suma(*args):
    return sum(args)
print(suma(2,2,2))

def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg **2
    return total 
print(suma_cuadrados(1,2,3))

print("---------------------suma_absolutos----------------")

def suma_absolutos(*args):
    total = 0
    for arg in args:
        total += abs(arg)
    return total
    
print(suma_absolutos(-1, -2))

print("--------------numeros_persona --------------------------")

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
print(numeros_persona("irene", 1,2,3,2,1))