""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso
número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
em ordem crescente. """

lista=[]
escolha=''

lista.append(int(input('Digite um número: ')))
print('Número adicionado..')

while not escolha=='n':
    escolha=str(input('Quer continuar? [s/n] '))
    if escolha=='n':
        print(f'\nVocê digitou os valores {sorted(lista)}\n')
        break
    elif escolha=='s':
        print('Número adicionado..',end=' ')
        lista.append(int(input('Digite um número: ')))

    else:
        print('Opção inválida!',end=' ')
