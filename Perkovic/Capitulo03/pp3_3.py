'''Problema Prático 3.3
Traduza estas declarações em instruções if/else do Python:
(a)Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário,
exiba 'Definitivamente não é um ano bissexto.'
(b)Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não,
exiba 'Melhor sorte da próxima vez…'.'''

print ('item (a)')

ano = int(input('Informe o ano: '))

if ano % 4 == 0:
    
    print('Pode ser um ano bissexto.')

else:
    
    print('Definitivamente não é um ano bissexto.')

print('Fim do item (a)')

print('item (b)')

entrada = input('Escolha 6 números de 01 até 60 separendo por espaços: ')

bilhete = entrada.split()

print(bilhete)
loteria = ['5', '7', '15', '21', '28', '45']


if bilhete == loteria:
    
    print('Você ganhou!')

else:
    print('Melhor sorte da próxima vez.')

print('Fim do iten (b)')
