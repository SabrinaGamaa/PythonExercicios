# def leiaint(n):
#     n = input(n)
#     while True:
#         if n.isnumeric():
#             break
#         else:
#             print('\033[31mERRO! Digite um número válido!\033[m')
#             n = leiaint('Digite um número: ')
#     return n
#
#
# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        if msg.isnumeric():
            valor = int(msg)
            ok = True
        else:
            print('\033[31mERRO! Digite um número válido!\033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
