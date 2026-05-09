'''Problema Prático 3.10
Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os
valores negativos na lista. A função não deverá retornar nada.
>>> negatives([4, 0, -1, -3, 6, -9])
-1
-3
-9'''

def negativos(lista):
    for numero in lista:
        if numero < 0:
            print(numero)   


#teste
negativos([5, 4, 3, 2, 1, 0, -1, -2, -3])