""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na
sequencia. No final, mostre uma listagem de preços, organizando os dados em forma tabular. """

lista=('Notebook',500.00,'Mouse',50.00,'Teclado',50.00)

print('\n')

for c in range(0,len(lista)):
    if c%2==0:
        print(f'{lista[c]:.<30}',end='')
    else:
        print(f'R${lista[c]:>7.2f}')

print('\n')
