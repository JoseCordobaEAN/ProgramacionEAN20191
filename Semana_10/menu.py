from Semana_10.vectores import *

vectores = {}

def ingresar_vector():
    """
    Permite leer un vector del usuario

    :return: list of num el vector ingresado por el usuario
    """
    vector = []

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
    print('su vector es', vector)
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


def op_suma_vectores():
    mostrar_vectores()
    v1 = input('seleccione el primer vector ')
    v2 = input('seleccione el segundo vector ')

    print(suma_vectores(vectores[v1], vectores[v2]))


def principal():

    MENSAJE = '''Seleccione una opcion:
    0. Salir
    1. Ingresar Vector
    2. Mostrar Vectores
    3. Producto escalar
    4. Suma Vectores
    '''

    while True:
        opcion = input(MENSAJE)

        if opcion == '0':
            print('Gracielas')
            break
        elif opcion == '1':
            nombre = input('¿Cual es el nombre de su vector? ')
            vector = ingresar_vector()
            vectores[nombre] = vector

        elif opcion == '2':
            mostrar_vectores()

        elif opcion == '3':
            op_producto_escalar()
        elif opcion == '4':
            op_suma_vectores()

        else:
            print('Seleccione una opcion valida')


if __name__ == '__main__':
    principal()