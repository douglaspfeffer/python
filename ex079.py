""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso
número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
em ordem crescente. """

lista=[]
escolha=''

numero=(int(input('Digite um número: ')))
lista.append(numero)
print('Número adicionado..',end='')

while not escolha=='n':
    escolha=str(input('Quer continuar? [s/n] '))
    if escolha=='n':
        print(f'\nVocê digitou os valores {sorted(lista)}\n')
        break
    elif escolha=='s':
        numero=(int(input('Digite um número: ')))
        if numero not in lista:
            lista.append(numero)
            print('Número adicionado..',end=' ')
        else:
            print('Valor duplicado! Não vou adicionar...',end='')

    else:
        print('Opção inválida!',end=' ')
