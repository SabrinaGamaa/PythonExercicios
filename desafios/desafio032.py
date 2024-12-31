from datetime import date
n1 = int(input('Digite o ano: '))
if n1 == 0:
    n1 = date.today().year
    print('O ano atual é {}'.format(n1))
if n1 % 4 == 0 and n1 % 100 !=0 or n1 % 400 == 0:
    print('O ano {} é BISSEXTO!!'.format(n1))
else:
    print('O ano {} não é bissexto!'.format(n1))
