'''2.22 Escreva uma expressão envolvendo a string s contendo o último e o primeiro nome de uma pessoa — separados por um espaço em branco — 
que seja avaliada para as iniciais da pessoa. Se a string tivesse meu primeiro e último nome, a expressão seria avaliada como 'LP'.'''

s = 'Helder Ramos'

iniciais = s[0] + s[s.index(' ') + 1]

print(iniciais)