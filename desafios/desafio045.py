from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
sorteio = randint(0, 2)
print('''SUAS OPCÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Eu joguei {}'.format(itens[sorteio]))
print('Você jogou {}'.format(itens[jogador]))
if sorteio == 0: # pedra
    if jogador == 0:# PEDRA
        print('EMPATE!!!')
    elif jogador == 1: # PAPEL
        print('\033[32mVocê GANHOU!!!\033[m')
    elif jogador == 2: # TESOURA
        print('\033[31mEU ganhei!!\033[m')
    else:
        print('Jogada invalida!')

elif sorteio == 1: # papel
    if jogador == 0:
        print('\033[31mEU ganhei!!\033[m')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('\033[32mVocê GANHOU!!!\033[m')
    else:
        print('Jogada invalida!')

elif sorteio ==2: # tesoura
    if jogador == 0:
        print('\033[32mVocê ganhei!!!\033[m')
    elif jogador == 1:
        print('\033[31mEU ganhei!!!\033[m')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('Jogada invalida!')
print('-=' * 12)
