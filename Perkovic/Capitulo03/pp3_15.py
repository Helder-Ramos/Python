'''Problema Prático 3.15
Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos mostrados a seguir.
Use a função jump() do módulo ch3. Você conseguirá obter a imagem desenhada executando:
>>> import turtle
>>> s = turtle.Screen()
>>> t = turtle.Turtle()
>>> olimpíadas(t)'''

def olimpiadas(t):
    from ch3 import jump

    x = -200
    y = 0
    a = 3

    for i in range(2):
        for j in range(a):
            jump(t, x + (220 * j), y)
            t.circle(100)

        x = -100
        y = -100    
        a = 2

import turtle
s = turtle.Screen()
t = turtle.Turtle()
olimpiadas(t)

s.mainloop()