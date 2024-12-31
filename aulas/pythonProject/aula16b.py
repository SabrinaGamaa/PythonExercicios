a = (2, 5, 4)
b = (5, 8, 1, 2)
# junta a e b na ordem esquerda para direita
c = a + b
print(f'Quantas vezes aparece o numero 5: {c.count(5)}')
print(f'Junta A e B: {len(c)}')
print(c)
print(f'Em que posição o 2 aparece depois da posicao 1: {c.index(2, 1)}')

pessoa = ('Sabrina', 21, 'M', '55.5')
# del(pessoa) ISSSO APAGA TUPLAS
print(pessoa)
