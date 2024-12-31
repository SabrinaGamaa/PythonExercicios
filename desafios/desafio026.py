n1 = input('Digite seu nome completo: ')
nome = n1.strip().lower()

print('Quantas vezes aparece a letra a no nome {}\nAparece {} vezes'.format(n1, nome.count('a')))

posicao = nome.lower().find('a')
print('A letra a aparece na {}° posição'.format(posicao + 1))

posdireita = nome.lower().rfind('a')
print('A ultima letra a aparece na {}° posição'.format(posdireita + 1))
