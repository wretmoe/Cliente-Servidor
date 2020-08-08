"""
Nombre:circunferencia.py
Objetivo:Calcula la circunferencia con el radio al cuadrado
Autor:Erick Jose Verduzco Campos
Fecha: 28/07/2020
"""

#Importamos el math
import math as m

def calcularArea(valorRadio):
	return m.pi*m.pow(valorRadio,2)


def main():
	ciclo = 's'
	while ciclo  == 's' or ciclo == 'S':
		print("___---Programa para Calcular area de la circunferencia---___")
		vradio = int(input("Introduce el valor del radio: "))
		print("El area de la circunfernecia es a: {} es:{}".format(vradio,calcularArea(vradio)))
		ciclo =  input("Calcular otra vez? (s/n)")
	else:
		print("Programa finalizado")


if __name__ == "__main__":
	main()