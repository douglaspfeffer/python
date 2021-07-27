""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual foi a soma entre eles. (desconsiderando a flag) """

contadora=0
soma=0

while True:
    numero=int(input('Digite um número inteiro qualquer. [Digite 999 para parar]: '))
    if numero==999:
        break
    contadora=contadora+1
    soma=soma+numero
print(f'\nForam digitados {contadora} números e a soma entre eles é de {soma}!\n')
