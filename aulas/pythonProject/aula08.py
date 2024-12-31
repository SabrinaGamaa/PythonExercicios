#math = ceil - floor - trunc - pow - sqrt - factorial
#from math import sqrt
# import math
from math import sqrt, ceil, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {} arredondado para cima'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {:.3f} normal'.format(num, raiz))
print('A raiz de {} é igual a {} arrendondado para baixo'.format(num, floor(raiz)))

import random
num = random.random()
num2 = random.randint(1, 10)
print('Seu numero aleatorio é {}'.format(num2))
print(num)
