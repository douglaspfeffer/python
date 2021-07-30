""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas. """

lista=[]
listaPar=[]
listaImpar=[]
escolha=''

while True:
    numero=int(input('Digite um número: '))
    lista.append(numero)
    if numero%2==0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    
    while not escolha=='n':
        escolha=str(input('Deseja continuar? [s/n] '))

        if escolha=='s':
            numero=int(input('Digite um número: '))
            lista.append(numero)
            if numero%2==0:
                listaPar.append(numero)
            else:
                listaImpar.append(numero)
            
            escolha=str(input('Deseja continuar? [s/n] '))

        if escolha=='n':
            print(f'\nA lista é {lista}')
            print(f'A lista PAR é {listaPar}')
            print(f'A lista IMPAR é {listaImpar}\n')
            break
    break
