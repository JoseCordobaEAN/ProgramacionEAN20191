import sys

# Leemos y validamos el dividendo
dividendo = input('ingrese el dividendo ')
if dividendo.isnumeric():
    dividendo = float(dividendo)
else:
    print(dividendo, 'no es un numero')
    sys.exit()

# Leemos y validamos el divisor
divisor = input('ingrese el divisor ')
if divisor.isnumeric():
    divisor = float(divisor)
else:
    print(divisor, 'no es un numero')
    sys.exit()

# Validamos que el divisor no sea 0
if divisor != 0:
    resultado = dividendo / divisor
else:
    print('el divisor no puede ser 0')
    sys.exit()


print('{0} dividido {1} es {2}'.format(
    dividendo, divisor, resultado
))



