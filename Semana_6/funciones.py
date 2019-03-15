def ordenar_palabras(palabra_1, palabra_2, palabra_3):
    """
    (str, str, str) -< str

    Ordena lexicograficamente las palabras

    <<< ordenar_palabras('hola', 'mundo', 'python')
    'hola mundo python'

    :param palabra_1:
    :param palabra_2:
    :param palabra_3:
    :return:
    """
    if palabra_1 < palabra_2 < palabra_3:
        return palabra_1 + ' ' + palabra_2 + ' ' + palabra_3
    elif palabra_1 < palabra_3 < palabra_2:
        return palabra_1 + ' ' + palabra_3 + ' ' + palabra_2
    elif palabra_2 < palabra_3 < palabra_1:
        return palabra_1 + ' ' + palabra_2 + ' ' + palabra_3
    elif palabra_2 < palabra_1 < palabra_3:
        return palabra_2 + ' ' + palabra_1 + ' ' + palabra_3
    elif palabra_3 < palabra_1 < palabra_2:
        return palabra_3 + ' ' + palabra_1 + ' ' + palabra_2
    else:
        return palabra_3 + ' ' + palabra_2 + ' ' + palabra_1


def un_segundo(hora, minuto, segundo):
    """
    (int, int, int) -> str

    Calcula la hora un segundo despues de los valores ingresados

    >>> un_segundo(10, 23, 42)
    'Son las 10 horas 23 minutos y 43 segundos'

    >>> un_segundo(10, 23, 59)
    'Son las 10 horas 24 minutos y 0 segundos'

    >>> un_segundo(23, 59, 59)
    'Son las 0 horas 0 minutos y 0 segundos'


    :param hora: La hora actual
    :param minuto: Los minutos actuales
    :param segundo: Los segundos actuales
    :return: str con el mensaje solicitado
    """
    siguiente_segundo = segundo + 1
    siguiente_minuto = minuto
    siguiente_hora = hora

    if siguiente_segundo >= 60:
        siguiente_segundo = 0
        siguiente_minuto += 1

        if siguiente_minuto >= 60:
            siguiente_minuto = 0
            siguiente_hora += 1

            if siguiente_hora >= 24:
                siguiente_hora = 0

    return 'Son las {0} horas {1} minutos y {2} segundos'\
        .format(siguiente_hora, siguiente_minuto, siguiente_segundo)


def len_adecuada(palabra, desde, hasta):
    """

    (str, int, int) -> str

    Valida si la longitud de la palabra está en el rango deseado

    >>> len_adecuada('hola', 0, 100)
    'La longitud de hola, está entre 0 y 100'
    >>> len_adecuada('hola', 1, 2)
    'La longitud de hola, no está entre 1 y 2'


    :param palabra:
    :param desde:
    :param hasta:
    :return:
    """
    return 'La longitud de {0}, {1}está entre {2} y {3}'\
        .format(palabra, "" if desde <= len(palabra) <= hasta else "no ", desde, hasta)
