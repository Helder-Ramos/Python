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


# (a)'ant bat cod'

a = s1 + ' ' + s2 + ' ' +s3
print(a)

# (b)'ant ant ant ant ant ant ant ant ant ant'

b = (s1 + ' ') * 9 + s1
print(b)

# (c)'ant bat bat cod cod cod'

c = s1 + ' ' + (s2 + ' ') * 2 + (s3 + ' ' ) * 2 + s3
print(c)


# (d)'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'

d = (s1 + ' ' + s2 + ' ') * 6 + s1 + ' ' + s2
print(d)

# (e)'batbatcod batbatcod batbatcod batbatcod batbatcod

e = (s2 * 2 + s3 + ' ') * 4 + (s2 * 2 + s3)
print(e)