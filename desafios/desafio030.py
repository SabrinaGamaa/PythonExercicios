cores = {'limpa': '\033[m',
         'Amarelo': '\033[1;33;40m',
         'verde': '\033[1;32m'}
n1 = int(input('Digite um número inteiro: '))
resto = n1 % 2
if resto == 0:
    print('Seu número é {}PAR{}!!!'.format(cores['Amarelo'], cores['limpa']))
else:
    print('Seu número é {}IMPAR{}!!!'.format(cores['verde'], cores['limpa']))

