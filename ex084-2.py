""" Faça um programa que leia o peso e nome de várias pessoas, guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves """

temp=[]
princ=[]

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo vocÊ cadastrou {len(princ)}')
print(f'O maior peso foi de {mai}Kg. Peso de ',end='')
for p in princ:
    if p[1]==mai:
        print(f'[{p[0]}]',end=' ')
print()
print(f'O peso menor foi de {men}Kg. Peso de ',end='')
for p in princ:
    if p[1]==men:
        print(f'[{p[0]}]',end=' ')
print()
