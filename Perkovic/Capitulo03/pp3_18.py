'''3.18 Repita o exercício anterior com o requisito adicional de que 'NÃO OK' é exibido na tela se
a condição for falsa.

O exercício anterior era:

3.17 Suponha que a, b e c tenham sido definidas no shell interativo conforme mostrado:
>>> a, b, c = 3, 4, 5
Dentro do shell interativo, escreva instruções if que exibem 'OK' se:
(a)a for menor que b.
(b)c for menor que b.
(c)A soma de a e b for igual a c.
(d)A soma dos quadrados de a e b for igual ao quadrado de c.'''

a, b, c = 3, 4, 5

if a < b:
    print('OK')
else:
    print('Not OK')

if c < b:
    print('OK')
else:
    print('Not OK')

if (a + b) == c:
    print('OK')
else:
    print('Not OK')

if (a**2 + b**2) == c**2:
    print('OK')
else:
    print('Not OK')