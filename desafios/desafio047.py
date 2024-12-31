from time import sleep
print('Vou mostrar todos os números pares de 1 até 50:')
for pares in range(1, 51):
    print('.', end='')
    sleep(0.5)
    if pares % 2 == 0:
        print(pares, end=' ')
print('Prontinho!')
