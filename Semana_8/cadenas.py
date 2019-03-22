def es_vocal(letra):
    """
    Valida si una letra es vocal

    >>> es_vocal('a')
    True
    >>> es_vocal('b')
    False
    >>> es_vocal('ae')
    Traceback (most recent call last):
    ..
    ValueError: ae no es una letra
    >>> es_vocal('1')
    Traceback (most recent call last):
    ..
    ValueError: 1 no es una letra

    :param letra:
    :return:
    """
    if (len(letra) == 1 and letra.isalpha()):
        return letra in 'aeiouAEIOU'
    raise ValueError(letra + ' no es una letra')


def contar_vocales(cadena):
    """
    Cuenta las vocales en una cadena

    >>> contar_vocales('hola')
    2

    >>> contar_vocales('Duque')
    3

    >>> contar_vocales('qwqwqwq')
    0

    :param cadena:
    :return:
    """
    contador = 0
    for letra in cadena:
        if es_vocal(letra):
            contador += 1
    return contador


def contar_consonantes(cadena):
    """
    Cuenta las vocales en una cadena

    >>> contar_consonantes('hola')
    2

    >>> contar_consonantes('Duque')
    2

    >>> contar_consonantes('qwqwqwq')
    7

    :param cadena:
    :return:
    """
    return len(cadena) - contar_vocales(cadena)

def contar_todo(lista):
    """
    (list of str) -> list of int

    Cuenta la cantidad de vocales y consonantes en la lista de cadenas


    >>> contar_todo(['hola', 'mundo'])
    [4, 5]

    >>> contar_todo(['jose', 'manuel', 'cordoba', 'castillo'])
    [11, 14]

    :param lista: la lista de palabras a evaluar
    :return: lista de enteros donde la primera pos contiene el número de vocales y la segunda
    el numero de consonantes

    """
    # resultado = [0,0]
    # for palabra in lista:
    #     resultado[0] += contar_vocales(palabra)
    #     resultado[1] += contar_consonantes(palabra)
    # return resultado
    vocales = 0
    consonantes = 0
    for palabra in lista:
        vocales += contar_vocales(palabra)
        consonantes += contar_consonantes(palabra)
    return [vocales, consonantes]
