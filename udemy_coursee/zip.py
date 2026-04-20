nombres = ['Jesus', 'Celia', 'Eva', 'irene']
edades = [65, 60, 36, 26]
ciudades = ['Armuña', 'Armuña', 'Armuña', 'Armuña']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    if nombre == 'Celia':
        print(f'{nombre} tenia {edad} años y vivia en {ciudad}.')
    else:
        print(f'{nombre} tiene {edad} años y vive en {ciudad}.')

