""" A Confederação Nacional de Natação precisa de um progama que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER """

import datetime
anoatual=datetime.date.today().year
anodenascimento=int(input('Digite o ano do seu nascimento: '))
idade=anoatual-anodenascimento

if idade>=0 and idade<=9:
    print('Você tem {} anos. Logo você está na categoria MIRIM'.format(idade))
elif idade>9 and idade<=14:
    print('Você tem {} anos. Logo você está na categoria INFANTIL'.format(idade))
elif idade>14 and idade<=19:
    print('Você tem {} anos. Logo você está na categoria JUNIOR'.format(idade))
elif idade>19 and idade<=25:
    print('Você tem {} anos. Logo você está na categoria SÊNIOR'.format(idade))
elif idade>25:
    print('Você tem {} anos. Logo você está na categoria MASTER'.format(idade))
else:
    print('Ano de nascimento inválido! Estamos atualmente em {}'.format(anoatual))
