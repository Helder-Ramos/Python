'''3.16 Use a função eval() para avaliar essas strings como expressões Python:
(a)'2 * 3 + 1'
(b)'hello'
(c)"'hello' + 'not'+ 'world!'"
(d)"'ASCII'.count('I')"
(e)'x = 5'''

a = eval('2 * 3 + 1')
print(a)

# b = eval('hello')
print('b apresenta erro porque o Python tenta avaliar hello como uma variável e não como string.')

c = eval("'hello' + 'not'+ 'world!'")
print(c)

d = eval("'ASCII'.count('I')")
print(d)

# e = eval('x = 5')
print('e apresenta erro de sitaxe pois a função eval não avalia instruções, apenas expressões')