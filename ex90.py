#  Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

listaDicionario={}

listaDicionario['Nome']=str(input('Nome: '))
listaDicionario['Média']=float(input('Média de {}: '.format(listaDicionario['Nome'].capitalize())))

if listaDicionario['Média']>=7:
    listaDicionario['Situação']='Aprovado'
elif listaDicionario['Média']>=5 and listaDicionario['Média']<7:
    listaDicionario['Situação']='Recuperação'
else:
    listaDicionario['Situação']='Reprovado'

for k,v in listaDicionario.items():
    print(f'{k} é igual a {v}')
