from time import sleep

def lista1(inicio, fim, passo):
    print('-=' * 25)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}' )
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')


lista1(1, 10, 1)
lista1(10, 0, 2)
print('-=' * 25)
print('Agora é sua vez de pesonalizar a contagem!')
lista1(inicio = int(input('Início: ')), fim = int(input('Fim: ')), passo = int(input('Passo: ')))


