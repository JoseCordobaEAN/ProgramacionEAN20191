# Solicitar el nombre
nombre = input('Ingrese su nombre ')

# Solicitar el valor de la hora trabajada
valor_hora = input('¿A como la hora? ')
valor_hora = int(valor_hora)

# Solicitar la cantidad de horas trabajadas
horas_trabajadas = input('¿Cuantas horas trabajo? ')
horas_trabajadas = int(horas_trabajadas)

# Imprimir el mensaje con el nombre y la remuneración del trabajador
salario = valor_hora * horas_trabajadas


# print('su salario es'+ salario)
print(nombre, 'su salario es', salario)
