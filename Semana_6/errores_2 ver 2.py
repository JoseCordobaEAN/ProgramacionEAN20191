try:
    dividendo = float(input('ingrese el dividendo '))
    divisor = float(input('ingrese el divisor '))

    resultado = dividendo / divisor

    print('{0} dividido {1} es {2}'.format(
        dividendo, divisor, resultado
    ))

except ZeroDivisionError:
    print('el divisor no puede ser 0')

except ValueError as e:
    print(e)