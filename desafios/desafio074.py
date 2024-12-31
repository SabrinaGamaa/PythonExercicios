from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10),
               randint(0, 10), randint(0, 10))
print(f'Os números sorteados são:')
for f in sorteio:
     print(f'{f}', end=' ')
print(f'\nO maior número sorteado foi {max(sorteio)}')
print(f'O menor número sorteado foi {min(sorteio)}')

