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
     letras = set(string)
     return sorted(letras)
print(ordenar("entretenido"))

print("-------------------0 repetido-----------------")

def repetido(*args):
     
     for i in range(len(args)- 1): 
        
        if args[i] == 0 and args[i + 1] == 0:
             return True
     return False
print(repetido(5,6,1,0,9,3,5))
    