from Semana_10.menu import ingresar_vector

matrices = {}

def leer_matriz():
    """
    Lee una matriz por teclado
    :return: (list of list of int) la matriz del usuario
    """
    resultado = []
    while True:
        entrada = input('Desea ingresar una fila? s/n ')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector()[1:])
    return resultado


while True:

    MENU = """
    **********Menu**********
    0. Salir
    1. Ingresar Matriz
    2. Ver Matrices
    ************************
    """

    seleccion = input(MENU)
    if seleccion == '0':
        print('Suerte')
        break
    elif seleccion == "1":
        nombre = input('cual es el nombre de su matriz ')
        matriz = leer_matriz()
        matrices[nombre] = matriz
    elif seleccion == "2":
        print('Sus matrices')
        for matriz in matrices:
            print(matriz, "=")
            print(matrices[matriz])
    else:
        print("Seleccion invalida")

