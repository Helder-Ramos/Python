'''2.24 Escreva a expressão ou instrução Python relevante, envolvendo uma lista de números lst e usando operadores e
métodos de lista para estas especificações.
(a)Uma expressão que é avaliada como o índice do elemento do meio de lst
(b)Uma expressão que é avaliada como o elemento do meio de lst
(c)Uma instrução que classifica a lista lst em ordem decrescente
(d)Uma instrução que remove o primeiro número da lista lst e o coloca no final'''

lst = [1, 2, 3, 4, 5]

a = len(lst)//2

print(a)

b = lst[a]

print(b)

lst.sort(reverse=True)

print(lst)

lst.append(lst.pop(0))

print(lst)