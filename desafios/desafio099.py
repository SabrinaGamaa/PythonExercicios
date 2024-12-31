from time import sleep
def maior(* num):
    print('-=' * 25)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) <= 0:
        print('Não tivemos nenhum número analisado')
    else:
        mai = max(num)
        print(f'E o maior número analisado foi {mai}')
    sleep(1)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
