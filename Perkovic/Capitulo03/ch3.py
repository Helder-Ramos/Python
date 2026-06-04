import turtle
from turtlefunctions import jump

def f(x):
    'retorna x**2 + 1'
    return x**2 + 1 # calcula x**2 + 1 e retorna valor obtido

def hello(name):
    'uma função hello personalizada'
    print('Hello, ' + name + '!')

print(help(f))

print(help(hello))

def g(x):
    x = 5

def h(lst):
    lst[0] = 5


def emoticon(t, x, y):
    'tartaruga t desenha uma carinha na coordenada (x, y)'

    # direção da tartaruga e tamanho da caneta
    t.pensize(3)
    t.setheading(0)

    # move para (x, y) e desenha cabeça
    jump(t, x, y)
    t.circle(100)

    # desenha olho direito
    jump(t, x + 35, y + 120)
    t.dot(25)

    # desenha olho esquerdo
    jump(t, x - 35, y + 120)
    t.dot(25)
    
    # desenha sorriso
    jump(t, x - 60.62, y + 65)
    t.setheading(-60)
    t.circle(70, 120)


s = turtle.Screen()
t = turtle.Turtle()
emoticon(t, -100, 100)
emoticon(t, 150, 100) 

turtle.mainloop()