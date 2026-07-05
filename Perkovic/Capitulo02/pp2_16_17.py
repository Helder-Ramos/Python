'''2.16 Escreva as instruções de atribuição Python correspondentes a:
(a)Atribuir 6 à variável a e 7 à variável b.
(b)Atribuir à variável c a média das variáveis a e b.
(c)Atribuir à variável estoque a lista contendo as strings 'papel', 'grampos' e 'lápis'.
(d)Atribuir às variáveis primeiro, meio e último as strings 'John', 'Fitzgerald' e 'Kennedy'.
(e)Atribuir à variável nomecompleto a concatenação das variáveis de string primeiro, meio e último.
Lembre-se de incorporar os espaços em branco de modo apropriado.'''

a = 6
b = 7
c = (a + b)/ 2
estoque = ['papel', 'grampos', 'lápis']
primeiro, meio, ultimo = 'John', 'Fitzgerald', 'Kennedy'
nomecompleto = primeiro + ' ' + meio + ' ' + ultimo

print(a, b, c, estoque, primeiro, meio, ultimo, nomecompleto, sep='\n')

'''2.17 Escreva expressões Booleanas correspondentes às instruções lógicas a seguir e avalie as expressões:
(a)A soma de 16 e –9 é menor que 10.
(b)O comprimento da lista inventário é mais de cinco vezes o comprimento da string nomecompleto.
(c)c não é maior que 24.
(d)6,75 está entre os valores dos inteiros a e b.
(e)O comprimento da string meio é maior que o comprimento da string primeiro e menor que o comprimento da string último.
(f)Ou a lista estoque está vazia ou tem mais de 10 objetos nela.'''

a17 = 16 + (-9) < 10

b17 = len(estoque) > 5 * len(nomecompleto)

c17 = c <= 24

d17 = a < 6.75 < b

e17 = len(primeiro) < len(meio) < len(ultimo)

f17 = estoque == [] or len(estoque) > 10

print(a17, b17, c17, d17, e17, f17, sep='\n')