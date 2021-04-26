import math

class FormaGeometrica:
	__slots__ = ()
	def get_area(self):
		raise NotImplementedError(NotImplemented)
	def get_perimetro(self):
		raise NotImplementedError(NotImplemented)


class Circulo(FormaGeometrica):
    '''
    >>> c = Circulo()
    >>> c.raio = 2  # ok
    >>> c.lado = 2  
    # AttributeError
    '''
    __slots__ = ("raio")
    def __init__(self):
        super()
        self.raio = None
    
    def get_perimetro(self):
        return 2 * math.pi * self.raio
    
    def get_area(self):
        return math.pi * self.raio ** 2


    

