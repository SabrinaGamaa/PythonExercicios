'''Escrava um progama que leia um número n iinteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia
de FIBONACCI'''
n1 = int(input('Digite quantos termos: '))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')
