while True:
    dato = input('ingresa tu dato')
    print(dato)
    if dato.isnumeric() and int(dato) % 2 != 0:
        break