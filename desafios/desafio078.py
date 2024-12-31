# num = ([int(input('Digite um número: '))],
#        [int(input('Digite outro número: '))],
#        [int(input('Digite mais um número: '))],
#        [int(input('Digite o ultimo número: '))])
# print(f'O maior número é {max(num)} na {num.index(max(num))}ª posição')
# print(f'O menor número é {min(num)} na {num.index(min(num))}ª posição')

cont = []
men = mai = 0
for c in range(0, 5):
    cont.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        mai = men = cont[c]
    else:
        if cont[c] > mai:
            mai = cont[c]
        if cont[c] < men:
            man = cont[c]
print('-=' * 30)

print(f'Os números digitados: {cont}')
print(f'O maior numero é o {mai} nas posição', end='')
for i, v in enumerate(cont):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor número é o {men} nas posição ', end='')
for i, v in enumerate(cont):
    if v == men:
        print(f'{i}...', end='')

