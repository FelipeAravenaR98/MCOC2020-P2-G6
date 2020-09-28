import numpy as np

g = 9.81 #kg*m/s^2


class Barra(object):

	"""Constructor para una barra"""
	def __init__(self, ni, nj, R, t, E, ρ, σy):
		super(Barra, self).__init__()
		self.ni = ni
		self.nj = nj
		self.R = R
		self.t = t
		self.E = E
		self.ρ = ρ
		self.σy = σy

	def obtener_conectividad(self):
		"""Implementar"""
		return [self.ni, self.nj]

	def calcular_area(self):
        
		A = 3.14*(self.R**2) - 3.14*((self.R-self.t)**2)
        
		return A

	def calcular_largo(self, reticulado):

            ret = reticulado
            xi = ret.xyz[self.ni]
            xj = ret.xyz[self.nj]
            L = np.sqrt((xi[0]-xj[0])**2 + (xi[1]-xj[1])**2 )

            return L        
		
    
	

	def calcular_peso(self, reticulado):
        
            L = self.calcular_largo(reticulado)
            A = self.calcular_area()
            
            
            return self.ρ * A * L * g









