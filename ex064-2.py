""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando a flag) """

quantidadeNumerosDigitados=0
soma=0

numero=int(input('Digite um número inteiro qualquer: '))

while numero!=999:

    soma=soma+numero
    quantidadeNumerosDigitados=quantidadeNumerosDigitados+1
    numero=int(input('Digite um número inteiro qualquer: '))

print('\nQuantidade de números digitados: {}'.format(quantidadeNumerosDigitados))
print('A soma dos números digitados é {}\n'.format(soma))
