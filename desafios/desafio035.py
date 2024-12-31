from time import sleep
print('-=-' * 20)
print('Analisador de triângulo.')
print('-=-' * 20)
n1 = float(input('Digite o cateto adjacente: '))
n2 = float(input('Digite o cateto: '))
n3 = float(input('Digite o terceiro: '))
print('ANALISANDO...')
sleep(2.5)
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos  acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
