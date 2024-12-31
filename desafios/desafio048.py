print('Vamos calulcar a soma entre todos os números ímpares que são multiplos de três. No intervalo de 1 a 500:')
soma = 0
cont = 0
for imp in range(1, 501, 2):
    if imp % 3 == 0:
        soma += + imp
        cont += + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
