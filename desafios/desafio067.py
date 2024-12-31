'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('--' * 25)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 25)
    if num <= -1:
        break
    for tabuada in range(1, 11):
        print(f'{num} x {tabuada} = {num * tabuada}')
print('PROGRAMA DA TABUADA ENCERRADA. Volte sempre!')
