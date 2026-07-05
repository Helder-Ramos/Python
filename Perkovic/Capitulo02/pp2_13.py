'''Comece avaliando, no shell interativo, a atribuição:
>>> s1 = '-'
>>> s2 = '+'

Agora, escreva expressões de string envolvendo s1 e s2 e os operadores de string + e * que são
avaliados como:
(a)'-+'
(b)'–+'
(c)'+––'
(d)'+––+––'
(e)'+––+––+––+––+––+––+––+––+––+––+'
(f)'+–+++––+–+++––+–+++––+–+++––+–+++––'
Tente tornar suas expressões de string as menores possíveis.'''

s1 = '-'
s2 = '+'

a = s1 + s2

b = a

c = s2 + (s1 * 2)

d = 2 * c

e = 10 * c + s2

f = (s2 + b + s2 + c) * 5

print(a, b, c, d, e, f, sep='\n')