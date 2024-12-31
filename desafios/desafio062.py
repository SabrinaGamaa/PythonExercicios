n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão da PA: '))
termo = n1
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        cont += 1
        termo += n2
    print('PAUSE')
    mais = int(input('Quantos termos a mais você quer? '))
print('{}'.format(total))
