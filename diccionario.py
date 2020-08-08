"""
Nombre:diccionario.py
Objetivo:Muestra la operación de los diccionarios en python
Autor:Erick Jose Verduzco Campos
Fecha:05/08/2020
"""

#¿Qué es un diccionario?
"""
Un diccionario es una estructura de datos que almacena valores heterogeneos
pero los almacena como en un formato de clave:valor. Quiere decir que cada elemento del diccionario 
se almacena como una lista de pares key:valor.
Por ejemplo: 'nombre':'Erick Jose Verduzco Campos' 
No son mutables, it does mean no cambian. Una vez que los creamos permanecerán con los mismos valores
No podremos introducir más datos.
"""

def main():
    #Creamos un diccionario con distintos key y datos
    dic = {'clave':20082133, 'nombre':'Erick Jose Verduzco Campos', 'edad':54, 'cursos':['Python', 'Progra Web', 'IA']}
    #Listar items del diccionario
    print("Los items son: ", dic)
    #Imprimir un item de un diccionario proporcionando su key
    print("El valor de la key es: ", dic['nombre'])
    #Imprimir los valores de todas las keys del diccionario
    for i in dic:
        print(i, ":", dic[i])
    
    #En el caso de la lista incluidas como un item del diccionario, lo accesamos
    for i in dic['cursos']:
        print(i)

    #Investigar los métodos los diccionarios y correrlos en el programa. get, pop, key, clean, items, update


if __name__ == "__main__":
    main()