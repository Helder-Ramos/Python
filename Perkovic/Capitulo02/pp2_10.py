'''Problema Prático 2.10
Escreva expressões Python correspondentes ao seguinte:
(a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm
comprimentos a e b
(b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
(c)A área de um disco com raio a
(d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
dentro de um círculo com centro (a, b) e raio r'''

import math


# (a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm
# comprimentos a e b
hipotenusa = (a**2 + b**2)**(1/2)

# ou

hipotenusa = math.sqrt(a**2 + b**2)

# (b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5

hipotenusa == 5

#(c)A área de um disco com raio a

area_disco = math.pi * a**2

# (d)O valor da expressão Booleana que verifica se um ponto com coordenadas 
# x e y está dentro de um círculo com centro (a, b) e raio r

((x - a)**2 + (y - b)**2)**2 <= r**2