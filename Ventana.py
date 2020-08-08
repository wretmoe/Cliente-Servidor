"""
Nombre:Ventana.py
Objetivo:Muestra como se trabajan ventanas GUI en Python TKinter
Autor:Erick Jose Verduzco Campos
Fecha:29/07/2020
"""

#Importar las librerias de tkinter
from tkinter import*
from tkinter import ttk


#Funcion para enviar datos al servidor echo
def sendToServer():
	print("Se enviaron los datos")

#Funcion main
def main():
	#Creamos la ventana contenedora
	win = Tk()

	#Modificacomos parámetros de la ventana win
	win.geometry("400x400")
	win.title("Mi Primera Ventana en Python TKinter!!!")

	#Creamos etiqueta
	label = ttk.Label(win, text="Texto para enviar al server").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)

	#Creamos un boton para enviar el contenido de la propiedad text del Entry al servidor
	ttk.Button(win, text="Enviar mensaje", command=sendToServer).pack(side=BOTTOM)

	#Creamos un boton  y lo colocamos en la ventana
	ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)

	#Hacemos un ciclo para dibujar y esperar eventos
	win.mainloop()



#Función main
if __name__=="__main__":
	main()