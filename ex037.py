""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão:
1 para binário
2 para octal
3 para hexadecimal """

numero=int(input('Digite um número inteiro qualquer: '))

print('Deseja converter para: ')
print('1- Binário\n2- Octal\n3- Hexadecimal')
escolha=int(input('Qual é a sua escolha? '))

if escolha==1:
    print('O número {} em BINÁRIO é {}'.format(numero,bin(numero)[2:]))
elif escolha==2:
    print('O número {} em OCTAL é {}'.format(numero,oct(numero)[2:]))
elif escolha==3:
    print('O número {} em HEXADECINAL é {}'.format(numero,hex(numero)[2:]))
else:
    print('Número inválido')
