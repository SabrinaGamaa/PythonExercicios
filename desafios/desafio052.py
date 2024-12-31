print('VAMOS DESCOBRIR SE O NÚMERO É PRIMO')
tot = 0
num = int(input('Digite um número inteiro: '))
for n1 in range(1, num + 1):
    if num % n1 == 0:
        print('\033[1;32m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(n1), end=' ''\033[m')
print('\nO número {} foi dividido por {} vezes'.format(num, tot))
if tot == 2:
    print('E é por isso que ele é PRIMO')
else:
    print('E é por isso que ele NÃO é primo')
