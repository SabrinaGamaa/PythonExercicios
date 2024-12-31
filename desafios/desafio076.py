produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 32.90)
print('=' * 30)
print(f'{"LOJA SABRINA":^30}')
print('=' * 30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}', end=' ')
    else:
        print(f'R${produtos[pos]:>6.2f}')
print('-' * 30)