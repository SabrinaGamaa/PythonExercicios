'''from random import choice
n1 = int(input('Digite um número de 0 a 5: '))
n2 = [0, 1, 2, 3, 4, 5]
n = choice(n2)
print('Vamos fazer o sorteio!!!!!!!')
if n1 == n:
    print('Parabéns!!! você escolheu o número {} e o número sorteado é {}'.format(n1, n))
else:
    print('Infelizmente você escolheu o número {} e o sorteado é {}.'.format(n1, n))
print('-----------FIM-----------')'''
from random import randint #sorteia um número
from time import sleep #faz o computador pensar
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2.5)
if computador == jogador:
    print('Parabéns você escolheu {} e o número sorteado é {}'.format(jogador, computador))
else:
    print('Infelizmente você escolheu o {} e sorteado é {}'.format(jogador, computador))
