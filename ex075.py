""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

a) Quantas vezes apareceu o número 9
b) Em que posição foi digitado o número 3
c) Quais foram os números pares """

lista=(int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: ')))

print(f'\nO número 9 apareceu {lista.count(9)} vezes')

if 3 in lista:
    print(f'O número 3 apareceu na {lista.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

for c in lista:
    if c%2==0:
        print(f'Os números pares são: {c}')
