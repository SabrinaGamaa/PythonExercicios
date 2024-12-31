lista = [[], []]
valor = 0
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}ª número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-=' * 30)
lista[0].sort()
lista[1].sort()
print(f'Os pares são: {lista[0]}')
print(f'Os impar são: {lista[1]}')

# print(lista)
# print('Números PARES: ', end='')
# for pares in lista:
#     lista.sort()
#     if pares % 2 == 0:
#         print(f'{pares}', end=' ')
# print('\nNúmeros IMPARES: ', end=' ')
# for impar in lista:
#     lista.sort()
#     if impar % 2 == 1:
#         print(f'{impar}', end=' ')


