'''2.27 Usando a técnica do Exercício 2.26, escreva instruções Python que desenham um losangocom 100 pixels de 
comprimento de lado usando Turtle graphics.'''

# observação pessoal: considerando que o quadrado é também um losango, acredito que o livro queira um quadrado orientado em 45º
# em relação ao eixo x

import turtle

s = turtle.Screen()
t = turtle.Turtle()


t.left(60)

for i in range(2):
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)

s.bye()