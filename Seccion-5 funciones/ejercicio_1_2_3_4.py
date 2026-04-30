def devolver_distintos(a,b,c):
        suma = a+b+c
        lista = [a,b,c]

        if suma > 15:
            return max(lista)
        elif suma < 10:
            return min(lista)
        elif suma >10 and suma< 15:
            return sorted(lista)[1]
    

print(devolver_distintos(1, 2, 3 ))


print("-------------------.ordenar letras-----------------")

def ordenar(string):
     letras = list(string)
     return sorted(letras)
print(ordenar("entretenido"))