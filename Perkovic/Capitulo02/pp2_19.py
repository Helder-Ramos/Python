'''2.19 Um alvo de dardos de raio 10 e a parede em que está pendurado são representados usando o sistema de coordenadas bidimensionais, 
com o centro do alvo na coordenada (0,0). As variáveis x e y armazenam as coordenadas x e y de um lançamento de dardo. Escreva uma 
expressão usando as variáveis x e y que avalia como True se o dardo atingir o (estiver dentro do) alvo, e avalie a expressão para estas
 coordenadas do dardo:
(a)(0, 0)
(b)(10, 10)
(c)(6, –6)
(d)(–7, 8)'''

raio = 10

# item a
x, y = 0, 0

a = (x**2 + y**2)**(1/2) < raio

print(a)

# item b
x, y = 10, 10

b = (x**2 + y**2)**(1/2) < raio

print(b)

# item c
x, y = 6, -6

c = (x**2 + y**2)**(1/2) < raio

print(c)

# item d
x, y = -7, 8

d = (x**2 + y**2)**(1/2) < raio

print(d)