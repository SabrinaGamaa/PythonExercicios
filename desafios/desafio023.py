n1 = input('Digite um número de 0 a 9999: ')
n1 = n1.zfill(4)
print('Unidade: {}'.format(n1[3]))
print('Dezena: {}'.format(n1[2]))
print('Centena: {}'.format(n1[1]))
print('Milhar: {}'.format(n1[0]))