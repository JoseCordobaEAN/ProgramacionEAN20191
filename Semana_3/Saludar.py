# Creamos una varible con el mensaje
mensaje = '¿Cual es tu nombre? '

# La función input nos permite recibir una cadena, imprimirla
# Y capturar la entrada del usuario
nombre = input(mensaje)

# Imprimimos el saludo (note que la función print puede trabajar con
# multiples parámetros)
#print('Hola', nombre, 'Bienvenido a python')
print('Hola '+ nombre+ ' Bienvenido a python')