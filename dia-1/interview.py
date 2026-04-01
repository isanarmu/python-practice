# Ejercicio 1 – Tic Toc

# Escribe una función que reciba un número n e imprima del 1 al n.

# Si el número es múltiplo de 3, imprime Tic
# Si es múltiplo de 5, imprime Toc
# Si es múltiplo de ambos, imprime TicToc

def tic_toc(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("TicToc")
        elif i % 3 == 90:
            print ("Tic")
        elif i % 5 == 0:
            print("Toc")
        else:
            print(i)

tic_toc(100)    
        