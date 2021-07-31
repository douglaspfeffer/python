""" Faça um programa que leia o peso e nome de várias pessoas, guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves """

lista=[]
quantidadePessoas=0
escolha=''


nome=str(input('Digite um nome: '))
lista.append(nome.capitalize())
quantidadePessoas=quantidadePessoas+1
peso=float(input(f'Digite o peso de {nome.capitalize()}: '))
lista.append(peso)

maiorPeso=peso
menorPeso=peso

while not escolha=='n':
    escolha=str(input('Deseja continuar? [s/n] '))

    if escolha=='n':
        print(f'\n{quantidadePessoas} pessoas foram cadastradas')
        break

    elif escolha=='s':
        nome=str(input('Digite um nome: '))
        lista.append(nome.capitalize())
        quantidadePessoas=quantidadePessoas+1
        peso=float(input(f'Digite o peso de {nome.capitalize()}: '))
        lista.append(peso)
        if peso>=maiorPeso:
            maiorPeso=peso
        else:
            menorPeso=peso

    else:
        print('Escolha inválida!',end=' ')

print(f'O maior peso é {maiorPeso} de ',end='')

for p in range(0,len(lista),2):
    if p%2==0:
        if lista[p+1]==maiorPeso:
            print(f'[{lista[p]}]',end=' ')

print(f'\nO menor peso é {menorPeso} de ',end='')

for p in range(0,len(lista),2):
    if p%2==0:
        if lista[p+1]==menorPeso:
            print(f'[{lista[p]}]',end=' ')
print('\n')
