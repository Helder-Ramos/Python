'''Acrescente a docstring retorna a média de x e y à função média() e a
docstring exibe os números negativos contidos na lista lst à
função negativos() dos Problemas Práticos 3.8 e 3.10. Verifique seu trabalho usando a
ferramenta de documentação help(). Você deverá receber, por exemplo:
>>> help(média)
Ajuda sobre a função média no módulo __main__:
média(x, y)
retorna a média de x e y'''


def media(x, y):
    '''retorna a média de x e y'''
    return (x + y) / 2

def negativos(lst):
    '''exibe os números negativos contidos na lista lst'''
    for numero in lst:
        if numero < 0:
            print(numero)  

#teste
help(media)

help(negativos)
