""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de
acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida """

from math import pow

peso=float(input('Digite o peso: '))
altura=float(input('Digite a altura: '))
imc=peso/pow(altura,2)
if imc<18.5:
    print('Seu IMC é {:.2f}. Logo você está ABAIXO do peso ideal.'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu IMC é {:.2f}. Logo você está NO PESO IDEAL.'.format(imc))
elif imc>=25 and imc<30:
    print('Seu IMC é {:.2f}. Logo você está em SOBREPESO.'.format(imc))
elif imc>=30 and imc<=40:
    print('Seu IMC é {:.2f}. Logo você está na OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f}. Logo você está na OBESIDADE MÓRBIDA.'.format(imc))
