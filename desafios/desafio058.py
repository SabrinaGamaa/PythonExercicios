from random import randint
pensar = randint(0, 10)
print('Tente adivinhar um número de 0 a 10 que eu estou pensando.')
n1 = int(input('Digite o número: '))
palpites = 1
while pensar != n1:
    n1 = int(input('Você errou! Tente novamente: '))
    palpites += 1
    if n1 > pensar:
        print('Vou te ajudar, pensa em um número MENOR...')
    elif pensar > n1:
        print('Vou te ajudar, pensa em um número MAIOR...')
print('-=' * 30)
print('Você ganhou!! Eu pensei no número {} e você digitou {}'.format(pensar, n1))
print('Você precisou de {} palpites.'.format(palpites))

#while not acertou: