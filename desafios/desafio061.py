n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1
    termo = termo + n2
print('FINALIZADO!')
