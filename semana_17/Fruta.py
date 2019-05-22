class Fruta:

    sabor = ''
    cantidad = 0
    pelada = False
    __TIPOS__ = ['banano', 'manzana', 'pera', 'piña', 'papaya']


    def __init__(self, sabor, cantidad):
        """
        Crea una nueva fruta

        :param sabor: cadena con el tipo de fruta
        :param cantidad: La cantidad de fruta en inventario
        """
        self.sabor = sabor
        self.cantidad = cantidad


    def pelar(self):
        """
        Pela la fruta si no esta pelada
        :return: El estado de la fruta
        """
        if not self.pelada:
            self.pelada = True
            return self.pelada
        raise ValueError('La fruta ya esta pelada')


    def cortar(self, cantidad_usar):
        '''
        Corta la fruta si esta pelada, retorna la cantidad de fruta pelada

        :param cantidad_usar: la cantidad de fruta a usar
        :return: la cantidad obtenida para esa fruta
        '''
        pass


    def licuar(self, cantidad_usar):
        """
        licua la fruta si esta pelada, retorna la cantidad de fruta pelada

        :param cantidad_usar: la cantidad de fruta a usar
        :return: la cantidad de zumo obtenida para esa fruta
        """
        pass