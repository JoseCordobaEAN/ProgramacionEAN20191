pizza_carnes = ['jamon', 'salchicha', 'salami']
pizza_pollo = ['pollo', 'tocineta', 'champiñones']

pizza_especial = pizza_carnes + pizza_pollo

print(pizza_especial)

pizza_mega_carnes = pizza_carnes * 3
print(pizza_mega_carnes)

pizza_ultra_mega_carnes = pizza_carnes * 20
print(pizza_ultra_mega_carnes)

pizza_especial_extra_pollo = pizza_pollo * 2 + pizza_carnes
print(pizza_especial_extra_pollo)

print('la pizza especial tiene mani?', 'mani' in pizza_especial)

pizza_pollo.append("Ciruela")
print(pizza_pollo)

pizza_pollo.insert(2, 'queso')
print(pizza_pollo)

ciruela = pizza_pollo.pop()
print(pizza_pollo)

pizza_pollo.remove('queso')
print(pizza_pollo)

pizza_ultra_mega_carnes.remove('jamon')
print(pizza_ultra_mega_carnes)

pos_pollo = pizza_pollo.index('pollo')
print(pos_pollo)

pos_pollo = pizza_pollo.index('queso')
print(pos_pollo)
