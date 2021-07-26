""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem menos de 20 anos """

idadeMedia=0
idadeHomemVelho=0
nomeHomemVelho=''
quantidadeMulherMenos20=0

for c in range(1,4+1):
    nome=str(input('\nDigite o nome da pessoa {}: '.format(c))).strip()

    idade=int(input('Digite a idade de {}: '.format(nome)))
    idadeMedia=idadeMedia+idade

    sexo=str(input('Digite o sexo de {}. F ou M: '.format(nome))).lower().strip()

    if c==1 and idade>=0 and sexo=='m' or sexo=='masculino':
        nomeHomemVelho=nome
        idadeHomemVelho=idade
    else:
        if idade>idadeHomemVelho and sexo=='m' or sexo=='masculino':
            nomeHomemVelho=nome
            idadeHomemVelho=idade
    
    if c==1 and idade<20 and sexo=='f' or sexo=='feminino':
        quantidadeMulherMenos20=quantidadeMulherMenos20+1
    else:
        if idade<20 and sexo=='f' or sexo=='feminino':
            quantidadeMulherMenos20=quantidadeMulherMenos20+1

print('A idade média do grupo é de {:.2f} anos'.format(idadeMedia/4))
print('O nome do Homem mais velho é: {}, {} anos'.format(nomeHomemVelho,idadeHomemVelho))
print('{} mulheres tem menos de 20 anos'.format(quantidadeMulherMenos20))
