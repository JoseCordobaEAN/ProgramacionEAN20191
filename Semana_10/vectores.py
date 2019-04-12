def producto_escalar(escalar, vector):
    """

    >>> producto_escalar(2, [1, 2, 3])
    [2, 4, 6]

    :param escalar:
    :param vector:
    :return:
    """
    res = []
    cont = 0
    while cont < len(vector):
        res.append(escalar * vector[cont])
        cont += 1
    return res