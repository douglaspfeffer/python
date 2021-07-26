""" Escreva um prograama que leia um número n inteiro e mostre na tela os n primeiros elementos de uma
sequência de fibonacci
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 """

numeroDeTermos=int(input('Digite um número de termos que você quer mostrar: '))

termo1=0
termo2=1

print('{} -> {}'.format(termo1,termo2),end='')

contadora=3

while contadora<=numeroDeTermos:
    termo3=termo1+termo2
    print(' -> {}'.format(termo3),end='')
    termo1=termo2
    termo2=termo3
    contadora=contadora+1

print(' -> Fim')
