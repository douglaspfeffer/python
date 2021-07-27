""" Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO
vai continuar. No final mostre:

a) qual é o total gasto na compra.
b) quantos produtos custam MAIS de R$1000
c) qual é o NOME do produto mais BARATO """

totalGasto=0
mais1000=0
nomeProdutoMaisBarato=''
precoProdutoMaisBarato=0
contador=0

while True:
    nome=str(input('Digite o nome do produto: '))
    preco=float(input('Digite o preço do produto R$: '))
    contador=contador+1
    totalGasto=totalGasto+preco

    if contador==1:
        precoProdutoMaisBarato=preco
        nomeProdutoMaisBarato=nome
    else:
        if preco<precoProdutoMaisBarato:
            precoProdutoMaisBarato=preco
            nomeProdutoMaisBarato=nome

    if preco>1000:
        mais1000=mais1000+1
    
    escolha=str(input('Deseja continuar? [s/n]: ')).lower().strip()
    if escolha=='n':
        break

print(f'\nO total gasto na compra é {totalGasto}')
print(f'{mais1000} produtos custam mais de R$1000')
print(f'{nomeProdutoMaisBarato.capitalize()} é o produto mis barato')
print('Fim do programa')
