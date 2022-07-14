import numpy as np
import random

def crear_archivo():
    with open('numeros_prueba.txt','w') as text_file:
        for i in range(20):
            if i==19:
                text_file.write(str(random.randint(100,1000)))
            else:
                text_file.write(str(random.randint(100,1000))+',')

def leer_archivo():
    with open('numeros_prueba.txt','r') as text_file:
        lines = text_file.read().split(',')
        return lines

def obtener_impares(lista_numeros_prueba):
    lista_numeros_impares = []
    for numero in lista_numeros_prueba:
        if int(numero) % 2 != 0:
            lista_numeros_impares.append(numero)
    return lista_numeros_impares

def mostrar_resultados(lista_numeros_impares):
    
    print('Lista Final: ')
    print(lista_numeros_impares)
    print('\n')
    print('Dimensión de la lista:')
    print(np.size(lista_numeros_impares))

def main():

    crear_archivo()
    lista_numeros_prueba = leer_archivo()
    lista_numeros_impares = obtener_impares(lista_numeros_prueba)
    mostrar_resultados(lista_numeros_impares)
    
if __name__ == "__main__":
    main()