'''Problema Prático 3.14 
Implemente a função trocaPU(), que aceita uma lista como entrada
 e troca o primeiro e último elementos da lista. Você pode considerar que a lista não 
 estará vazia. A função não deverá retornar nada. 
 >>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs'] 
 >>> trocaPU(ingredientes) 
 >>> ingredientes ['maçãs', 'açúcar', 'manteiga', 'farinha'] '''

def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

print('Lista ingredientes antes da chamada da função: ')
print(ingredientes)

trocaPU(ingredientes)

print('Lista ingredientes após a da chamada da função: ')
print(ingredientes)