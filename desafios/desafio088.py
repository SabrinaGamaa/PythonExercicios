from random import randint
from time import sleep
lista = []
tot = 1
jogos = []
print('-' * 30)
print(f'{'JOGO DA MEGA SENA':^30}')
print('-' * 30)
escolha = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= escolha:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {escolha} JOGOS ', '-=' * 3)
for i, v in enumerate(jogos):
    print(f'Jogo {i + 1}: {v}')
    sleep(1)
print('-=' * 5, end='')
print(f'  BOA SORTE  ', end='')
print('-=' * 5)

