""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto  """

sexo=''

while sexo!='m' and sexo!='f':
    sexo=str(input('Digite o seu sexo [M ou F]: '))
print('Parabéns, {} é um sexo válido :)'.format(sexo.upper()))
