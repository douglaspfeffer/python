""" Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """

matriz=[[0,0,0],[0,0,0],[0,0,0]]

somaPar=0
somaValoresTerceiraColuna=0
maiorValorSegundaLinha=0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para a linha {linha+1} coluna {coluna+1}: '))
        if linha==1:
            if matriz[linha][coluna]>=maiorValorSegundaLinha:
                maiorValorSegundaLinha=matriz[linha][coluna]
        if matriz[linha][coluna]%2==0:
            somaPar=somaPar+matriz[linha][coluna]
        if coluna==2:
            somaValoresTerceiraColuna=somaValoresTerceiraColuna+matriz[linha][coluna]

for linha in range(0,3):
    print()
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')

print(f'\n\nA soma dos números pares são: {somaPar}')
print(f'A soma dos valores da terceira coluna são: {somaValoresTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorValorSegundaLinha}')
print('\n')
