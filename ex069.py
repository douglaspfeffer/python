""" Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o USUÁRIO quer ou não continuar. No final mostre:

a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos. """

contadorMaioridade=0
contadorHomens=0
quantidadeMulheresMenos20Anos=0

while True:
    idade=int(input('\nDigite sua idade: '))
    sexo=str(input('Digite o seu sexo [m/f]: ')).strip().lower()
    if idade>18:
        contadorMaioridade=contadorMaioridade+1
    if sexo=='m':
        contadorHomens=contadorHomens+1
    if sexo=='f' and idade<20:
        quantidadeMulheresMenos20Anos=quantidadeMulheresMenos20Anos+1
    
    continuar=str(input('\nDeseja continuar? Sim ou Não [s/n]: ')).strip().lower()
    if continuar=='n':
        break

print(f'\n{contadorMaioridade} pessoas tem mais de 18 anos')
print(f'{contadorHomens} homens foram cadastrados')
print(f'{quantidadeMulheresMenos20Anos} mulheres tem menos de 20 anos')
print('\nFim do programa')
