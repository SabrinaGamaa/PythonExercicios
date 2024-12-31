n1 = float(input('Digite a sua velocidade: '))
if n1 >= 81:
    multa = (n1 - 80) * 7
    print('Você será multado em R${:.2f} por ter andado acima da velocidade permitida.'.format(multa))
else:
    print('Siga seu caminho!')
