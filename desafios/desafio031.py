n = float(input('Quantos KM você percorreu: '))
if n >= 200:
    print('Você percorreu {}km e gastou R${:.2f} de gasolina.'.format(n, n * 0.45))
else:
    print('Você percorreu {}km e gastou R${:.2f} de gasolina.'.format(n, n * 0.50))
