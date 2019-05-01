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

def suma_vectores(v1, v2):
    """
    Suma dos vectores

    >>> suma_vectores([1,2,3], [3, 2, 1])
    [4, 4, 4]

    :param v1:
    :param v2:
    :return:
    """

    if len(v1) == len(v2):
        retorno = []
        for i in range(len(v2)):
            retorno.append(v1[i] + v2[i])
        return retorno
    raise ValueError('los vectores tienen dif longitud')