'''Problema Prático 2.10
Escreva expressões Python correspondentes ao seguinte:
(a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm
comprimentos a e b
(b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
(c)A área de um disco com raio a
(d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
dentro de um círculo com centro (a, b) e raio r'''

'''(a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm
comprimentos a e b'''

import math

cateto_01 = 4
cateto_02 = 3

hipotenusa = math.sqrt((cateto_01**2 + cateto_02**2))

print(hipotenusa)

'''(b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5'''

print(hipotenusa == 5)

'''(c)A área de um disco com raio a'''

raio = 5

area_circulo = math.pi * raio**2

print(area_circulo)

'''(d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
dentro de um círculo com centro (a, b) e raio r'''



origemx = 2
origemy = 3
raio = 5

coordenadax = 6
coordenaday = 4

raio_coordenada = math.sqrt(((coordenadax - origemx)**2 + (coordenaday - origemy)**2))

print(raio_coordenada < raio)