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
    pass