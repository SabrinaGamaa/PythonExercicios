soma = 0
cont = 0
for num in range(1, 7):
    n1 = int(input('Digite o {}° número: '.format(num)))
    if n1 % 2 == 0:
        soma = soma + n1
        cont = cont + 1

print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
print('FIM')