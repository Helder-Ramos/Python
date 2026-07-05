'''2.26 Escreva instruções Python que desenham um quadrado com 100 pixels de lado usando Turtle graphics.
Não se esqueça de importar o módulo turtle primeiro. As duas primeiras e a última instrução deverão ser conforme mostrado:
>>>s = turtle.Screen() # cria tela
>>>t = turtle.Turtle() # cria tartaruga
...
# agora escreve uma sequência de instruções...
# que desenha o quadrado
>>> s.bye() # remove a tela quando termina'''

import turtle

s = turtle.Screen()
t = turtle.Turtle()


for i in range(4):
    t.forward(100)
    t.left(90)

s.bye()