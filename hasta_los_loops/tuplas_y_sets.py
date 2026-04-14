# numero de veces que aparece algo
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

# Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
mi_tupla = (1, 2, 3, 4)

a, b, c, d = mi_tupla
print(mi_tupla)

# SETS, solo admiten elementos unicos, en un set los elementos no se pueden repetir, si añades un elemento repetido python lo omiten
# no pueden almacenar listas ni diccionarios
# NO tienen un ORDEN interno
mi_set = set([1, 2, 3, 4, 5,5])
print(mi_set)
print(type(mi_set))

otro_tipo_set = {1, 2, 3, 4, 5}
print(otro_tipo_set)
print(type(otro_tipo_set))
# print(otro_tipo_set[0]) ESTO va a dar ERROR prqeu no tienen orden
# se pueden imprimir tuplas y strings dentro de sets pero diccionaarios no. SOLO admite elementos INMUTABLES. Las lsitas y los diccionarios si pueden mutar
set_2 = set([1, "hola", (2, 4)])
print(set_2)
print(1 in set_2)
# para unir sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
s3.add(10)
s3.remove(2) #se puede usar .discard apra que si ese elemento que intentas eliminar no existe no te de error
s3.clear() #borra todo
print(f"esta es la union: ", s3)