""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

a) Quantos números foram digitados
b) A lista de valores, ordenada de forma decrescente
b) Se o valor 5 foi digitado e está ou não na lista """

lista=[]
escolha=''
contador=1
contador5=0

lista.append(int(input('Digite um número: ')))

print('Número adicionado..')

while not escolha=='n':
    escolha=str(input('Quer continuar? [s/n] '))

    if escolha=='n':
        print(f'\nForam digitados {contador} números\n')
        print(f'A lista de valores, ordenada de forma decrescente {sorted(lista,reverse=True)}')
        break
    elif escolha=='s':
        contador=contador+1
        print('Número adicionado..',end=' ')
        lista.append(int(input('Digite um número: ')))

    else:
        print('Opção inválida!',end=' ')

if 5 in lista:
    print(f'O número 5 foi digitado {lista.count(5)} vezes\n')
else:
    print('O número 5 não foi digitado\n')
