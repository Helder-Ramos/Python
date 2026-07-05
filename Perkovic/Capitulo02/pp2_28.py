'''2.28 Usando a técnica do Exercício 2.26, escreva instruções Python que desenham um pentágono com 100 pixels de comprimento 
de lado usando Turtle graphics. Depois faça um hexágono, um heptágono e um octógono.'''

import turtle

n = 4
x = -1000

s = turtle.Screen()
t = turtle.Turtle()

for i in range(4):
    n = n + 1
    giro_angulo_interno = 180 - (180 * (n - 2))/n
    t.penup()
    x = x + 400
    t.goto(x, 0)
    t.pendown()
    for j in range(n):
        t.forward(100)
        t.left(giro_angulo_interno)

s.bye()