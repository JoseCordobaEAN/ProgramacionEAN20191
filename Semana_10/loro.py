dato = 2

while dato % 2 == 0:
    dato = input(' ingresa un dato ')
    print(dato)
    try:
        dato = int(dato)
    except:
        dato = 2

print('tu numero impar es', dato, 'chao')