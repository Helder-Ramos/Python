'''Problema Prático 3.1
Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe
a temperatura em graus Celsius usando a fórmula:
Celsius = 5/9 (Fahrenheit-32)
Seu programa deverá ser executado da seguinte forma:
>>> Digite a temperatura em graus Fahrenheit: 50
A temperatura em graus Celsius é 10.0'''

fahrenheit = eval(input('Digite a temperatura em graus Fahrenheit: '))

celsius = (fahrenheit-32) * 5/9

print('A temperatura em graus Celsius é', celsius)