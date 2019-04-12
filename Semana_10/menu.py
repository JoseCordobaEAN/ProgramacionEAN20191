from Semana_10.vectores import *

vectores = {}

def ingresar_vector():
    """
    Permite leer un vector del usuario

    :return: list of num el vector ingresado por el usuario
    """
    vector = [input('¿Cual es el nombre de su vector? ')]

    while True:
        num = input('Ingrese su escalar o "s" para terminar ')
        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print(num, 'no es un escalar')
        else:
            break
    print('su vector', vector[0], 'es', vector[1:])
    return vector


def mostrar_vectores():
    for nombre in vectores:
        print(nombre, 'contiene', vectores[nombre])

def op_producto_escalar():
    while True:
        escalar = input('Ingrese su escalar ')
        try:
            escalar = int(escalar)
            break
        except:
            print(escalar, 'no es un escalar')

    print('Cual es el nombre de su vector')
    mostrar_vectores()
    seleccion = input()

    print('El producto escalar es',
          producto_escalar(escalar, vectores[seleccion]))


def principal():

    MENSAJE = '''Seleccione una opcion:
    0. Salir
    1. Ingresar Vector
    2. Mostrar Vectores
    3. Producto escalar
    '''

    while True:
        opcion = input(MENSAJE)

        if opcion == '0':
            print('Gracielas')
            break
        elif opcion == '1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]

        elif opcion == '2':
            mostrar_vectores()

        elif opcion == '3':
            op_producto_escalar()

        else:
            print('Seleccione una opcion valida')


if __name__ == '__main__':
    principal()