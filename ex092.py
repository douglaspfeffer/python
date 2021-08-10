# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

listaDicionario={}

listaDicionario['Nome']=str(input('Nome: ')).strip().capitalize()
anoDeNascimento=int(input('Ano de Nascimento: '))
listaDicionario['Idade']=(date.today().year)-anoDeNascimento
listaDicionario['CTPS']=int(input('Carteira de Trabalho (CTPS) (0 para não tem): '))

if listaDicionario['CTPS']==0:
    print()
    print(listaDicionario)
    for k,v in listaDicionario.items():
        print(f'{k} tem o valor {v}')

if listaDicionario['CTPS']!=0:
    listaDicionario['Ano de Contratação']=int(input('Ano de Contratação: '))
    listaDicionario['Salário']=float(input('Salário: R$ '))
    listaDicionario['Aposentadoria']=listaDicionario['Ano de Contratação']-anoDeNascimento+35
    print()
    print(listaDicionario)
    for k,v in listaDicionario.items():
        print(f'{k} tem o valor {v}')
print()
