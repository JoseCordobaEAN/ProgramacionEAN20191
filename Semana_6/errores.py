numero = input('ingresa tu numero ')

try:

    print('tu numero {0} al cuadrado es {1}'.format(numero, float(numero) ** 2))

except:

    print("'{0}' no es un numero".format(numero))