import math

def area_circulo(radio):
    '''

    (num) -> float

    Calcula el area de un circulo dado el radio

    >>> area_circulo(1)
    3.141592653589793

    >>> area_circulo(3)
    9.42477796076938

    :param radio: num que representa el radio del circulo
    :return: float que representa el area del circulo
    '''
    area = radio * math.pi
    return area


def perimetro_triangulo(lado1, lado2, lado3):
    '''
    (num, num, num) -> num

    Calcula el perímetro de un triangulo dada la longitud de sus
    lados

    >>> perimetro_triangulo(1, 2, 3)
    6

    >>> perimetro_triangulo(1, 1, 1)
    3

    :param lado1: num la longitud del primer lado del triangulo
    :param lado2: num la longitud del segundo lado del triangulo
    :param lado3: num la longitud del tercer lado del triangulo
    :return: num la longitud del perimetro del triangulo
    '''
    return lado1 + lado2 + lado3


def semi_perimetro_triangulo(lado1, lado2, lado3):
    '''
    (num, num, num) -> num

    Calcula el semiperímetro de un triangulo dada la longitud de sus
    lados

    >>> semi_perimetro_triangulo(1, 2, 3)
    3.0

    >>> semi_perimetro_triangulo(1, 1, 1)
    1.5

    :param lado1: num la longitud del primer lado del triangulo
    :param lado2: num la longitud del segundo lado del triangulo
    :param lado3: num la longitud del tercer lado del triangulo
    :return: num la longitud del semiperimetro del triangulo
    '''
    return perimetro_triangulo(lado1, lado2, lado3) / 2


def area_triangulo(lado1, lado2, lado3):
    '''

    (num, num, num) -> num

    Calcula el area de un triangulo dada la longitud de sus lados

    >>> area_triangulo(1, 1, 1)
    0.4330127018922193

    >>> area_triangulo(4, 4, 5)
    7.806247497997997

    >>> area_triangulo(11, 7.5, 11)
    38.77897102489956


    :param lado1: num la longitud del primer lado del triangulo
    :param lado2: num la longitud del segundo lado del triangulo
    :param lado3: num la longitud del tercer lado del triangulo
    :return: num el area del triangulo
    '''
    s = semi_perimetro_triangulo(lado1, lado2, lado3) #s es el semiperimetro del triangulo
    s_lado1 = s - lado1
    s_lado2 = s - lado2
    s_lado3 = s - lado3
    area = s * s_lado1 * s_lado2 * s_lado3
    area **= (1/2)
    return area

def es_impar(num):
    '''

    num -> bool

    Determina si un numero es impar

    >>> es_impar(3)
    True

    >>> es_impar(9838)
    False


    :param num: el numero a evaluar
    :return: True si es impar False de lo contrario
    '''
    return num % 2 != 0

def es_par(num):
    '''

    num -> bool

    Determina si un numero es impar

    >>> es_par(3)
    False

    >>> es_impar(9838)
    True


    :param num: el numero a evaluar
    :return: True si es par False de lo contrario
    '''
    return not es_impar(num)