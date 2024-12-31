#from math import sqrt
#oposto = float(input('Digite a médida do cateto oposto: '))
#adjacente = float(input('Digite a medida do cateto adjacente: '))
#o1 = oposto**2
#a1 = adjacente**2
#real = o1 + a1
#print('O resultado é {:.2f}'.format(sqrt(real)))
from math import hypot
n1 = float(input('Digite o cateto oposto: '))
n2 = float(input('Digite o cateto adjacente: '))
real = hypot(n1, n2)
print('A soma do cateto oposto {} e o cateto adjacente {} a hipotenusa é: {}.'.format(n1, n2, real))
