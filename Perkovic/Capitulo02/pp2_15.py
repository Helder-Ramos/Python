'''2.15 Comece executando
s = 'goodbye'
Depois, escreva uma expressão Booleana que verifica se:
(a)O primeiro caractere da string s é 'g'
(b)O sétimo caractere de s é g
(c)Os dois primeiros caracteres de s são g e a
(d)O penúltimo caractere de s é x
(e)O caractere do meio de s é d
(f)O primeiro e último caracteres da string s são iguais
(g)Os 4 últimos caracteres da string s correspondem à string 'tion'
Nota: Essas sete instruções devem ser como True, False, False, False, True, False e False, respectivamente.'''

s = 'goodbye'

a = s[0] == 'g'

b = s[6] == 'g'

c = s[:2] == 'ga'

d = s[-2] == 'x'

e = s[(len(s)//2)] == 'd'

f = s[0] == s[-1]

g = s[-4:] == 'tion'

print(a, b, c, d, e, f, g)