# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.

listaDicionario={}
listaListaGols=[]
totalGols=0

listaDicionario['Nome']=str(input('Nome do jogador: ')).strip().capitalize()
totalPartidas=int(input(f'Quantas partidas {listaDicionario["Nome"]} jogou? '))

for c in range(0,totalPartidas):
    gol=int(input(f'Quantos gols na partida {c+1}? '))
    listaListaGols.append(gol)
    totalGols=totalGols+gol

listaDicionario['Gols']=listaListaGols[:]
listaDicionario['Total']=totalGols

print(f'\n{listaDicionario}\n')

for k,v in listaDicionario.items():
    print(f'O campo {k} tem o valor {v}')

print()

print(f'O jogador {listaDicionario["Nome"]} jogou {totalPartidas} partidas')
for p,g in enumerate(listaDicionario['Gols']):
    print(f'Na partida {p}, fez {g} gols')

print(f'Foi um total de {listaDicionario["Total"]} gols\n')
