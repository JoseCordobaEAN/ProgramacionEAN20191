from semana_16.introPOO import Casa

mi_casa = Casa('Calle 123 carrera 456')
casa_vecino = Casa('Calle 124 carrera 456')
casa_homero = Casa('Evergreen terrace 123, Springfield')

print(f'mi casa es {mi_casa}, la del vecino es {casa_vecino} y la de homero es {casa_homero}')

mi_casa.banos = 2
mi_casa.ambientes = 4

setattr(casa_vecino, 'banos', 3)
setattr(casa_vecino, 'ambientes', 6)

print(f'Mi casa tiene {mi_casa.ambientes} ambientes'
      f' La del vecino tiene {getattr(casa_vecino, "ambientes")}')

atributos = casa_homero.__dict__

for llave in atributos:
    print(f'Atributo {llave} con el valor {atributos[llave]} en la casa de homero')

setattr(casa_vecino, 'banos', 2)
setattr(casa_vecino, 'ambientes', 4)

if mi_casa == casa_vecino:
    print('mi casa y la del vecino son iguales')
else:
    print('mi casa y la del vecino son diferentes')