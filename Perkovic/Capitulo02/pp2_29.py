'''Usando a técnica do Exercício 2.26, escreva instruções Python que desenham os círculos sobrepostos com raio de 100 pixels,
mostrados a seguir, usando o Turtle graphics:
Os tamanhos dos círculos não importam; seus centros deverão ser, mais ou menos, os pontos de um triângulo equilátero.'''

import turtle

s = turtle.Screen()
t = turtle.Turtle()


t.circle(100)

t.penup()
t.goto(-50, -100)
t.pendown()

t.circle(100)

t.penup()
t.goto(50, -100)
t.pendown()

t.circle(100)

s.bye()