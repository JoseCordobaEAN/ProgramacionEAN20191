# Para definir listas utilizamos []
pizza = ['tomate', 'queso', 'peperroni', 'jamon', 'masa']

# Podemos ver nuestra lista
print(pizza)

# Podemos acceder a elementos en la lista utilizando
print('El cuarto elemento es ', pizza[3])

# Podemos obtener porciones de la lista con la siguiente notación
print('mi tajada de pizza tiene', pizza[1:3])

# También funciona si no conozco el final de la lista
print('mi tajada de pizza tiene', pizza[2:])

# O Si quiero ir de compienzo a una posición
print('mi tajada de pizza tiene', pizza[:3])

# Podemos obtener elementos de la lista en orden inverso
print('El ultimo elemento de mi pizza es', pizza[-1])

# O obetener porciones en orden inverso
print('El ultimo elemento de mi pizza es', pizza[-3:-1])

# Podemos modificar elementos de la lista
pizza[-1] = 'piña'
print(pizza)
# Por tanto la listas son mutables

# En Cambio las cadenas son inmutables
# cadena = 'Hola mundo'
# cadena[-1] = 'a'

