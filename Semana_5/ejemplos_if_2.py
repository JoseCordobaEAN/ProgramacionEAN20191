def mensaje_negativo(numero):
    """
    (float) -> str

    Escribe un mensaje para evaluar un numero negativo

    >>> mensaje_negativo(-10.0)
    'El numero es negativo'

    >>> mensaje_negativo(898)
    'El numero es positivo'

    :param numero: num el numero a evaluar
    :return: str con el mensaje de la evaluación
    """
    if numero < 0:
        return 'El numero es negativo'
    return 'El numero es positivo'

def compara_edades(edad1, edad2):
    """
    (int, int) -> str

    Genera un mensaje segun la diferencia de edad:
    la primera o la segunda mas joven o iguales

    >>> compara_edades(10, 20)
    'El primero es mas joven'

    >>> compara_edades(89, 56)
    'El segundo es mas joven'

    >>> compara_edades(56, 56)
    'Tienen la misma edad'

    :param edad1: int la edad del primero
    :param edad2: int la edad del segundo
    :return: mensaje asociado a la diferencia de edad
    """
    if edad1 > edad2:
        return 'El segundo es mas joven'
    elif edad1 == edad2:
        return 'Tienen la misma edad'
    else:
        return 'El primero es mas joven'


def es_parentesis(caracter):
    """

    (str of len == 1) -> str

    >>> es_parentesis('(')
    'Es parentesis'
    >>> es_parentesis('x')
    'No es parentesis'
    >>> es_parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: str el caracter a evaluar
    :return: str el mensaje de la validacion
    """
    if len(caracter) != 1:
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif caracter in '()': # caracter == '(' or caracter == ')':
        return 'Es parentesis'
    return 'No es parentesis'


def dividir(dividendo, divisor):
    '''

    (num, num) -> num

    Divide un numero entre otro

    >>> dividir(6, 2)
    3.0
    >>> dividir(1,0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: No dividiras por 0
    >>> dividir('hola', 100)
    Traceback (most recent call last):
    ..
    TypeError: hola no es un numero

    :param dividendo: num el dividendo a evaluar
    :param divisor: num el divisor a evaluar
    :return: la división entre dividendo y divisor
    '''
    if  int != type(dividendo) != float:
        raise TypeError(str(dividendo) + ' no es un numero')
    elif int != type(divisor) != float:
        raise TypeError(str(divisor) + ' no es un numero')
    elif divisor == 0:
        print('al pelo')
        raise ZeroDivisionError('No dividiras por 0')
    return dividendo / divisor