'''Problema Prático 3.2
Traduza estas instruções condicionais em instruções if do Python:
(a)Se idade é maior que 62, exiba 'Você pode obter benefícios de
pensão'.
(b)Se o nome está na
lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um
dos 5 maiores jogadores de beisebol de todos os tempos!'.
(c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
(d)Se pelo menos uma das variáveis
booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.'''

'''(a)Se idade é maior que 62, exiba 'Você pode obter benefícios de
pensão'.'''

idade = int(input('Informe sua idade: '))

if idade > 62:
    print('Você pode obter benefícios de pensão.')

print('Fim do item (a)')

'''(b)Se o nome está na
lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um
dos 5 maiores jogadores de beisebol de todos os tempos!'.'''

lista = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
nome = input('Informe o nome: ')

if nome in lista:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')

print('Fim do item (b)')

'''(c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.'''

golpes = float(input('Informe o valor dos golpes: '))
defesas = float(input('Informe o valor das defesas: '))

if golpes > 10 and defesas == 0:
    print('Você está morto...')

print('Fim do item (c)')

'''(d)Se pelo menos uma das variáveis
booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.'''

direcao = input('Informe um direção: ')

if direcao == 'norte' or direcao == 'sul' or direcao == 'leste' or direcao == 'oeste':
    print('Posso escapar.')

print('Fim do iten (d)')