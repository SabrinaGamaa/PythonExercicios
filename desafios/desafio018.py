from math import cos, tan, radians, sin
n1 = int(input('Qual o ângulo: '))
radiano = radians(n1)
seno = sin(radiano)
print('O ângulo de {} tem o SENO de {:.2f}'.format(n1, seno))
cosseno = cos(radiano)
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n1, cosseno))
tangente = tan(radiano)
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(n1, tangente))
