'''Problema Prático 3.3
Traduza estas declarações em instruções if/else do Python:
(a)Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 
'Definitivamente não é um ano bissexto.'
(b)Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez...'.'''
'''
# item (a)

ano = int(input('Informe o ano: '))

if ano % 4 == 0:
    print('Pode ser um ano bissexto.')

else:
    print('Definitivamente não é um ano bissexto.')


# item (b)

loteria = [1, 2, 3, 4]

bilhete = [1, 2, 3, 4]

if bilhete == loteria:
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez...')

'''
bilhete = input('informe o valor separado por espaços: ').split()

x = len(bilhete)

for i in range(x):
    bilhete[i] = int(bilhete[i])

print(bilhete)