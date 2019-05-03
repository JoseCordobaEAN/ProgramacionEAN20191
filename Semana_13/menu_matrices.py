from Semana_10.menu import ingresar_vector
from Semana_13.uso_archivos import *

RUTA_MATRICES = 'mis_matrices.json'
matrices = leer(RUTA_MATRICES)

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
        resultado.append(ingresar_vector())
    return resultado


def principal():
    """
    Funcion principal del menu

    :return: none
    """
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


    if guardar(RUTA_MATRICES, matrices):
        print('Se guardaron exitosamente sus matrices')
    else:
        print('No se han podido guardar las matrices')


if __name__ == '__main__':
    principal()

