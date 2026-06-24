'''Problema Prático 2.11
Comece executando estas instruções:
>>> s = turtle.Screen()
>>> t = turtle.Turtle(shape='turtle')
>>> t.penup()
>>> t.goto(-300, 0)
>>> t.pendown()
Deverá haver uma caneta de tartaruga no lado esquerdo da tela. Em seguida, execute uma
sequência de comandos turtle graphics do Python que produzirão esta imagem:'''

import turtle

s = turtle.Screen()

t = turtle.Turtle(shape='turtle')
t.penup()
t.goto(-300, 0)
t.pendown()

for i in range(9):
    t.setheading(-45)
    t.circle(50, 90)

t.penup()
t.goto(-100, 200)
t.pendown()
t.circle(50)
t.penup()
t.goto(0, -50)

t.penup()
t.goto(0, -50)

t.right(20)

s.mainloop()