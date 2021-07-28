""" Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados
b) Os 4 últimos colocados da tabela
c) Uma lista com os times em ordem alfabética
d) Em que posição na tabela está o time da Chapecoense """

lista=('Palmeiras','Atlético-MG','Fortaleza','Bragantino','Athletico-PR','Flamengo','Ceará SC','Atlético-GO','Bahia','Corinthians','Fluminense','Santos','Juventude','Internacional','Cuiabá','Sport Recife','São Paulo','América-MG','Grêmio','Chapecoense')

print(f'\nOs primeiros 5 colocados são: {lista[0:5]}')
print(f'Os 4 últimos da tabela são: {lista[-4:]}')
print(f'Os times em ordem alfabética é: {sorted(lista)}')
print('Chapecoense está na {}ª posição\n'.format(lista.index('Chapecoense')+1))
