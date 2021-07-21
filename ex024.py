'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'''

cidade=str(input('Digite o nome da cidade: '))

'''cidade.lower().strip().split()[0] >> vai transformar a palavra 'santo' em minúsculo,
vai remover os espaços inúteis, se existirem,e na posição 0 vai pesquisar pela palavra 'santo'
True=sim; False=não'''

print('A cidade começa com Santo? {}'.format('santo' in cidade.lower().strip().split()[0]))
