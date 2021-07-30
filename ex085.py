""" Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente. """

lista=[[],[]]

for c in range(1,7+1):
    numero=int(input(f'Digite o {c}º número: '))
    if numero%2==0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'\nOs valores PARES são: {sorted(lista[0])}')
print(f'Os valores IMPARES são: {sorted(lista[1])}\n')
