""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. """

lista=[]

for c in range(0,4+1):
    numero=int(input('Digite um número: '))
    if c==0 or numero>lista[len(lista)-1]:
        lista.append(numero)
        print('Número adicionado ao final da lista')
    else:
        pos=0
        while pos<len(lista):
            if numero<=lista[pos]:
                lista.insert(pos,numero)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos=pos+1
print(f'\nOs valores digitados em ordem foram: {lista}\n')
