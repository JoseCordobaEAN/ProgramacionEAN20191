# Para crear una clase usamos class
class Casa:

    def __init__(self, direccion):
        """

        :rtype: Casa
        :param direccion: 
        """
        self.banos = 0
        self.ambientes = 0
        self.direccion = direccion

    def __repr__(self):
        return f'Casa ubicada en {self.direccion}'


    def __eq__(self, other):
        return self.banos == other.banos and self.ambientes == other.ambientes

