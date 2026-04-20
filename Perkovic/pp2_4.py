'''Problema Prático 2.4
Comece executando as instruções de atribuição:
>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
(a)'ant bat cod'
(b)'ant ant ant ant ant ant ant ant ant ant'
(c)'ant bat bat cod cod cod'
(d)'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
(e)'batbatcod batbatcod batbatcod batbatcod batbatcod'''

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

a = s1 + ' ' + s2 + ' ' + s3
b = (s1 + ' ') * 9 + s1
c = (s1 +' ' ) * 1 + (s2 + ' ') * 2 + (s3 + ' ') * 2 + s3
d = (s1 + ' ' + s2 + ' ') * 6 + s1 + ' ' + s2
e = (s2 + s2 + s3 + ' ') * 4 + s2 + s2 + s3

print(a)
print(b)
print(c)
print(d)
print(e)