'''2.18 Escreva instruções Python correspondentes ao seguinte:
(a)Atribua à variável flores uma lista contendo as strings 'rosa', 'buganvília', 'iúca', 'margarida', 'dália' e 'lírio dos vales'.
(b)Escreva uma expressão Booleana que é avaliada como True se a string 'batata' estiver na lista flores e avalie a expressão.
(c)Atribua à lista espinhosas a sublista da lista flores consistindo nos três primeiros objetos na lista.
(d)Atribua à lista venenosas a sublista da lista flores consistindo apenas no último objeto da lista flores.
(e)Atribua à lista perigosas a concatenação das listas espinhosas e venenosas.'''

flores = ['rosa', 'buganvília', 'iúca', 'margarida', 'dália', 'lírio dos vales']

b = 'batata' in flores

espinhosas = flores[0:3]

venenosas = flores[-1:]

perigosas = espinhosas + venenosas

print(flores, b, espinhosas, venenosas,perigosas, sep='\n')
