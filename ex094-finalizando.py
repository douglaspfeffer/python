# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

listaDicionario={}
listaMulheres=[]
totalPessoasCadastradas=0

somaIdade=0
mediaIdade=0
quantidadeMulheres=0
escolha=''

while True:

    listaDicionario['Nome']=str(input('Nome: ')).strip().capitalize()
    listaDicionario['Sexo']=str(input('Sexo: [M/F] '))

    if listaDicionario['Sexo']=='f' or listaDicionario['Sexo']=='F':
        listaMulheres.append(listaDicionario['Nome'])
        quantidadeMulheres=quantidadeMulheres+1

    while listaDicionario['Sexo']!='m' and listaDicionario['Sexo']!='M' and listaDicionario['Sexo']!='f' and listaDicionario['Sexo']!='F':
        print('Opção inválida!',end=' ')
        listaDicionario['Sexo']=str(input('Sexo: [M/F] '))
        listaMulheres.append(listaDicionario['Nome'])
        quantidadeMulheres=quantidadeMulheres+1

    listaDicionario['Idade']=int(input('Idade: '))
    somaIdade=somaIdade+listaDicionario['Idade']
    totalPessoasCadastradas=totalPessoasCadastradas+1
    mediaIdade=somaIdade/totalPessoasCadastradas

    escolha=str(input('Deseja continuar? [S/N] '))

    while escolha!='s' and escolha!='S' and escolha!='n' and escolha!='N':
        print('Opção inválida!',end=' ')
        escolha=str(input('Deseja continuar? [S/N] '))
    
    if escolha=='n' or escolha=='N':
        break

if totalPessoasCadastradas==1:
    print(f'\n{totalPessoasCadastradas} pessoa foi cadastrada')
else:
    print(f'\n{totalPessoasCadastradas} pessoas foram cadastradas')

print(f'A média de idade é de {mediaIdade:.2f} anos')

if quantidadeMulheres==1:
    print(f'A mulhere cadastrada foi: {listaMulheres}')
else:
    print(f'As mulheres cadastradas foram: {listaMulheres}')

print('Lista de pessoas acima da média:')

    #break
