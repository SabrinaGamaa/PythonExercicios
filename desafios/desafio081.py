lista = []
cont = 0
cinco = ''
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    if 5 in lista:
        c = 'Tem o número 5 na lista.'
    else:
        c = 'Não tem o número 5 na lista.'
    sair = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while sair not in 'SN':
        sair = str(input('Tente novamente...Deseja continuar? [S/N]')).upper().strip()[0]
    if sair in 'N':
        break
print('=' * 30)
# print(f'Você digitou {len(lista)} elementos.')
print(f'Você digitou {cont} números.')
print(f'{c}')
lista.sort(reverse=True)
print(f'A lista de valores, ordenada de forma DECRESCENTE: {lista}')
