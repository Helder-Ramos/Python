s = input('Digite quadrado ou cubo: ')
if s == 'quadrado':
    def f(x):
        return x * x
else:
    def f(x):
        return x * x * x

print(f(3))