class Dummy:
	'''Solo sirve para el ejemplo'''

	def __init__(self, nombre) :
		self.__nombre__ = nombre # str


	def consultar (self) :
		# returns str
		return self.__nombre__

	def _protegida_ (self) :
		# returns str
		return 'esto esta protegido'

	def __privada__ (self) :
		# returns str
		return 'esto es privado'

	def __repr__(self):
		return self.consultar()


	def __eq__(self, other):
		if type(self) == type(other):
			return self.consultar() == other.consultar()
		raise TypeError(f'el tipo de {other} no es {type(self)}')
