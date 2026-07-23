'''3.17 Suponha que a, b e c tenham sido definidas no shell interativo conforme mostrado:
>>> a, b, c = 3, 4, 5
Dentro do shell interativo, escreva instruções if que exibem 'OK' se:
(a)a for menor que b.
(b)c for menor que b.
(c)A soma de a e b for igual a c.
(d)A soma dos quadrados de a e b for igual ao quadrado de c.'''

a, b, c = 3, 4, 5

if a < b:
    print('OK')

if c < b:
    print('OK')

if (a + b) == c:
    print('OK')

if (a**2 + b**2) == c**2:
    print('OK')