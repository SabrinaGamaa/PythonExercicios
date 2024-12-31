soma = mil = menor = cont = 0
barato = ' '
print('=' * 40)
print('{:^40}'.format('LOJA SABRINA'))
print('=' * 40)
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    soma += preco
    cont += 1
    if preco >= 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar adicionando? [S/N] ')).upper().strip()
    if sair == 'N':
        break
print('--' * 20)
print(f'Total da compra é de R${soma:.2f}')
print(f'{mil} produtos de sua compra custou mais de R$1000,00')
print(f'O produto mais barato é {barato} e está custando R${menor:.2f}')
