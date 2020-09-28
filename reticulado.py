
#PARTE RETICULADO
#GRUPO 6

#-------------------------------------------------------------------------

import numpy as np
from barra import Barra
class Reticulado(object):
    """Define un reticulado"""

    def __init__(self):
        super(Reticulado, self).__init__()
		
        self.xyz = np.zeros((0,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}

    def agregar_nodo(self, x, y, z=0):
        #Cambiar Tamaño
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        return
		
    def agregar_barra(self, barra):
        self.barras.append(barra)
        return

    def obtener_coordenada_nodal(self, n): 
        nodo = self.xyz[n]
        return nodo

    def calcular_peso_total(self):
        peso = 0.
        for a in self.barras:
            peso += a.calcular_peso(self)
        return peso

    def obtener_nodos(self):
        

        return self.xyz

    def obtener_barras(self):
        """Implementar"""
        return self.barras

    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        """Implementar"""
        return

    def agregar_fuerza(self, nodo, gdl, valor):
        """Implementar"""
        return

    def ensamblar_sistema(self):
        """Implementar"""
        return

    def resolver_sistema(self):
        """Implementar"""
        return

    def recuperar_fuerzas(self):
        """Implementar"""
        return


#-------------------------------------------------------------------------












