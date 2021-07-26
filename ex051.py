""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros
termos dessa progressão. """

primeiroTermo=int(input('Digite o primeiro: '))
razao=int(input('Digite a razão: '))

decimoTermo=primeiroTermo+(10-1)*razao

resposta=0

for c in range(primeiroTermo,decimoTermo+razao,razao):
    print(c,end=' -> ')
print('Fim')
