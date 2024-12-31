def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')

# Program principal
soma(3, 6)
soma(b=6, a=8)
soma(12, 9)
print('--' * 30)
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
def dobras(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobras(valores)
print(valores)