'''Escreva expressões Python correspondentes a estas instruções:
(a)A soma dos sete primeiros inteiros positivos
(b)A idade média de Sara (idade 65), Fátima (idade 56) e Mark (idade 45)
(c)2 à 20-ª potência
(d)O número de vezes que 61 cabe em 4356
(e)O resto de quando 4365 é dividido por 61'''

a = 1 + 2 + 3 + 4 + 5 + 6 + 7

Sara = 65
Fatima = 56
Mark = 45

b = (Sara + Fatima + Mark)/3

c = 2**20

d = 4356 // 61

e = 4365 % 61

print(a, b, c, d, e, sep='\n')