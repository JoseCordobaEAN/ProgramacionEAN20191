from Dummy import Dummy

mi_dummy = Dummy('Soy una prueba')
mi_otro_dummy = Dummy('Soy una prueba')

print(mi_dummy)

print(mi_dummy.consultar())

print(mi_dummy._protegida_())

print(mi_dummy.__privada__())

if mi_dummy == mi_otro_dummy:
    print('los dummys son iguales')
else:
    print('los dummys son diferentes')

print(f'el nombre de dummy es {getattr(mi_dummy, "__nombre__")}')

setattr(mi_dummy, 'prueba', 100)

print(mi_dummy.prueba)