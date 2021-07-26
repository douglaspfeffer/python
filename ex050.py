""" Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o """

soma=0

for c in range(1,6+1):
    numero=int(input('Digite o valor do número {}: '.format(c)))
    if numero%2==0:
        soma=soma+numero
print('A soma dos números pares é {}'.format(soma))
