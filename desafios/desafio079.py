lista = []
conti = 'S'
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')

    conti = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while conti not in 'SN':
        conti = str(input('Tente novamente...Quer continuar? [S/N] ')).upper().strip()[0]
    if conti == 'N':
        break
print('-=' * 35)
lista.sort()
print(f'Você digitou os valores {lista}')
