nombre = input('¿Cual es tu nombre? ')
amigo = input('¿Quien es tu amigo? ')

if len(nombre) > 10:
    print('Es un nombre muy largo')

print('''
    Esta es la historia de {0},
    
    Un día {0} salió a jugar baseball con {1} 
    vió
'''.format(nombre, amigo))