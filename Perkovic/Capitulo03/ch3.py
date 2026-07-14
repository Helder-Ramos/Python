def f(x):
    'retorna x**2 + 1'
    return x**2 + 1

def hello(name):
    'Uma função Hello personalizada'
    print('Hello ' + name + '!')

def g(x):
    x = 5

def h(lst):
    lst[0] = 5

def jump(t, x, y):
    'faz tartaruga saltar para coordenadas (x, y)'

    t.penup()
    t.goto(x, y)
    t.pendown()

def emoticon(t, x, y):
    'tartaruga t desenha uma carinha com queixo na coordenada (x, y)'
    #define a direção da tartaruga e tamanho da caneta
    t.pensize(3)
    t.setheading(0)

    # move para (x, y)
    jump(t, x, y)
    t.circle(100)

    # desenha o olho direito
    jump(t, x + 35, y + 120)
    t.dot(25)

    # desenha o olho esquerdo
    jump(t, x - 35, y + 120)
    t.dot(25)
    
    # desenha sorriso
    jump(t, x - 60.62, y + 65)
    t.setheading(-60)
    t.circle(70, 120)