dia = int(input('Quantos dias alugados: '))
km  = int(input('Quantos km foi percorrido: '))
d1 = dia * 60
k1 = km * 0.15
real = d1 + k1
print('O alguel do carro vai custar R${:.2f}'.format(real))
