"""
Nombre:Cilindro.py
Objetivo:Muestra como se trabajan objetos en python
Autor:Erick Jose Verduzco Campos
Fecha:30/07/2020
"""
from Circunferencia import Circunferencia

class Cilindro(Circunferencia):

    #Definimos el constructor
    def __init__(self, valorX, valorY, valorRadio, valorAltura):
        #Constructor de Circunferencia
        Circunferencia.__init__(self, valorX, valorY, valorRadio)
        #Constructor de Cilindro
        self.altura = valorAltura
    
    def getAltura(self):
        return self.altura

    def setAltura(self, valorAltura):
        self.altura = valorAltura

  
    def getVolumen(self):
        return self.getArea()*self.altura

    def toString(self):
        return Circunferencia.toString(self)+" la altura es :"+str(self.altura) + " y el volumen es: "+ str(self.getVolumen())       


c = Cilindro(2,3,4,7)
print(c.toString())