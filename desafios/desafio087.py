matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]
pares = 0
scol = 0
slin = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para as [{l},{c}] posição: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {scol}')
for c in range(0, 3):
    slin += matriz[1][c]
    if matriz[1][c] == 0:
        maior = matriz[1][c]
    else:
        if maior < matriz[1][c]:
            maior = matriz[1][c]
print(f'A soma da 2ª linha é {slin}')
print(f'O maior número da 2ª linha é {maior}')
