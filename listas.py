"""
Nombre:Listas.py
Objetivo:Muestra la función de las listas en python
Autor:Erick Jose Verduzco Campos
Fecha:04/08/2020
"""

def main():
    #Una lista es una estructura de datos en python
    #La ventaja aceptan datos de tipos distintos
    #Creamos una lista
    lista = [1,23.01, False, "Hola lista", "A",[-1,-5, "hola", 0.0], -12,"A"]
    # Lista Vacia
    listaVacia = []
    # Accesando a elementos de la lista
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)
    for i in listaVacia:
        print("El elemento de la lista es: ", elemento)
    #Imprimir un elemento de la lista
    print("Elemento en la posicion 3: ", lista[3])
    print("Elemento en la posicion -1: ", lista[-1])
    print(lista[-2])
    print(lista[5])
    #Leer elemento en la posicion 2 de la lista interna
    print(lista[5][2])

    #Metodos de las listas
    lista.append("Si se puede")
    print("---------------------------------------")
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)
    # count regresa el numero de veces que se repite un elememto en la lista
    print("Elemento se repite : " , lista.count("A"))

    # index() imprime el indice de un elemento en la lista
    print("La posicion de False es: ", lista.index(False))
    # Eliminar elementos de la lista : remove()
    lista.remove("Hola LIsta")
    for x in lista:
        print("El elemento de la lista es: ", x)


if __name__=="__main__":
    main()